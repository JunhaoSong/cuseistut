Generic Mapping Tools - Topographic Map
=======================================

Brief introduction
------------------

What is GMT?
************

#. The Generic Mapping Tools (GMT) is one of the most popular mapping softwares in the world;
#. It is widely used across the Earth, Ocean, and Planetary sciences and beyond;
#. It is a free, open source software licensed under the `GNU LGPL <https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License>`_ license.

.. image:: https://www.generic-mapping-tools.org/_static/gmt-logo.png
   :width: 80%

--------------------

What can GMT do?
****************

| 1. **Process data of different format.** For example, time series (seismograph), xy data (fault trace), xyz data(geographic data), and so on. 
| 2. **Generate publication-quality illustrations.** Here is an example: 

.. image:: https://docs.generic-mapping-tools.org/6.3/_images/ex07.png
   :width: 80%

| 3. **Automate workflows.** If script is provided and GMT is installed, one figure can be plotted by one command. 
| 4. **Make animations.** For example, this is an `animation <https://www.youtube.com/watch?v=H0RyjHRhJ3g>`_ showing Pacific Earthquakes in 2018 made by GMT. 

---------------------

How to install GMT?
*******************

.. note::

 | There are lots of ways to install GMT on your computer. 
 | Here we strongly suggest beginners to install it by `conda <https://docs.conda.io/en/latest/>`_. 

The following steps have been tested successfully for Linux, macOS, and window subsystem for linux.

| 1. **Install** `miniconda <https://docs.conda.io/en/latest/miniconda.html>`_
| 2. **Open a terminal and run these commands sequentially**

.. warning:: 

   Exclude $ and start without whitespace!

.. code:: 

 $ conda create --name gmt-env
 $ conda activate gmt-env
 $ conda install gmt -c conda-forge

| 3. **Check if it has been successfully installed**

.. code:: 

 $ gmt --version
 6.3.0

-------------

Start with three simple examples
********************************

| 1. Run this single command and look what will happen

.. code:: 

 $ gmt coast -Rg -JH15c -Gpurple -Baf -B+t"My First Plot" -pdf,png GlobalMap1

| 2. Run the following commands step-by-step and compare the difference

.. code:: 

 $ gmt begin GlobalMap2 png,pdf
 $ gmt coast -Rg -JH15c -Gpurple -Baf -B+t"My Second Plot"
 $ gmt end show

| 3. Run the same commands using Shell script and compare the difference

.. code:: 

 $ cat GlobalMap3.sh
 #!/bin/sh
 gmt begin GlobalMap3 png,pdf
 gmt coast -Rg -JH15c -Gpurple -Baf -B+t"My Third Plot"
 gmt end show
 $ sh GlobalMap3.sh

.. centered:: No difference found! And do you think which way is better, especially for very complex figures? There is no doubt that the third way, (i..e., based on script), is better. Since we can simply modify the script and re-run the script to refine the figure. 

---------

Basic structure of GMT script
*****************************

**Now let's take a further look at the third example in the previous part**

| 1. ``#!/bin/sh`` specifies **sh** as the command language interpreter.

.. tip:: 

 | $ which sh
 | If the output is /dir/to/sh, then replace ``#!/bin/sh`` by ``#!/dir/to/sh``

| 2. ``gmt begin GlobalMap3 png,pdf`` initiates a new GMT session. The output figure name is ``GlobalMap3``. The output figure format are ``png`` and ``pdf``.

.. note::

 | The sequence is important
 | That is: gmt begin <figure name> <format1,format2,...,formatN>

| 3. ``gmt coast -Rg -JH15c -Gpurple -Baf -B+t"My Third Plot"`` adds the first layer. If it's followed by other commands, as shown in later parts, this layer will be overlaid by new layers. 

.. note::

 | The general structure of these "adding-layer" commands is:
 | gmt <command> -<option1> -<option2> ..\. -<optionN>

| 4. ``gmt end show`` terminates the GMT session. If ``show`` exists, the produced figure of the first format will be opened by default viewer.

.. centered:: There are a lot of GMT commands and much much much more options. Here, this tutorial aims to give GMT beginners very quick training. Therefore, we will show readers how to generate figures from public seismic data using some commonly used commands. More specificlly, It includes: 1. Plotting topographic map 2. Plotting earthquake catalog 3. Plotting cross sections.

----------

Plotting topographic map
------------------------

Preview
*******

**After learning this part, you will be able to create the figure below or similar ones.** 

The figure below is modified from Figure 1 in `this paper <https://doi.org/10.1785/0320210041>`_.

.. image:: Banda_Arc_Region.png
   :width: 80%

It is generated using the following commands:

.. code:: 

 #!/bin/sh

 gmt begin Banda_Arc_Region png

 # constructing the frame
 gmt basemap -JM10c -R114/131/-14/-5 -BWeSn -Bxa5f1 -Bya2f1
 # creating a colormap with customized boundaries
 gmt makecpt -Crelief -T-6000/6000/200 -D -Z -H > elevation.cpt
 # plotting the topography data, which can be remotely obtained from gmt database using the @earth_relief_??? option
 gmt grdimage @earth_relief_01m -Celevation.cpt -I+
 # plotting the coastline data
 gmt coast -W0.5p,black -Da
 # inset a global figure with the specify boundary
 gmt inset begin -Dn1/0+jBR+w2.5c
 gmt coast -Rg -JG123/-10/90/? -B -Swhite -A5000 -Ggray -W0.2p,black -Da --MAP_FRAME_PEN=0.2p
 echo -e "\n114 -14\n131 -14\n131 -5\n114 -5\n114 -14" | gmt plot -W0.5p,red
 gmt inset end
 # plotting the trench data using given data file
 gmt plot java_trench.txt -W1p,white
 # inserting text
 echo '116 -12 Java trench' | gmt text -F+f8p,white
 # extracting stations locations from data files
 awk 'NR>1 {print $5,$6}' GE_3_stations.txt | gmt plot -Si6p -W0.1p,black -Gcyan
 awk -F"|" 'NR>3 {print $6,$5}' YS_30_stations.txt | gmt plot -Si6p -W0.1p,black -Gwhite
 # creating colorbar legend
 gmt colorbar -Dn1/0+o0.5c/0c+jBL+w5.5c -Bxa3000 -By+l"Topo (m)" -Celevation.cpt

 gmt end show

 rm elevation.cpt

To reproduce it by yourself, you may first download or save :download:`java_trench.txt <./java_trench.txt>`, :download:`GE_3_stations.txt <./GE_3_stations.txt>`, :download:`YS_30_stations.txt <./YS_30_stations.txt>`, and then move these files into your working directory. Try to copy the above commands and run them on your own computer to see if you can generate the same figure without warning or error.

Step-by-Step explanation
************************

| **1. gmt basemap -JM10c -R114/131/-14/-5 -BWeSn -Bxa5f1 -Bya2f1** to plot base maps and frames

``-JM10c`` specifies the map projection type to be `Mercator projection <https://docs.generic-mapping-tools.org/latest/cookbook/map-projections.html#jm>`_. The width of map is 10c (10 centimeters).

``-R114/131/-14/-5`` specifies the map range, minimum and maximum longitudes are 114 and 131, minimum and maximum latitudes are -14 -5. 

``-BWeSn`` specifies that the left and bottom ticklabels are visible, which the right and top ticklabels are invisible.

``-Bxa5f1`` specifies that x axes have ticklabels with interval of 5 and ticks with interval of 1.

``-Bya2f1`` specifies that y axes have ticklabels with interval of 2 and ticks with interval of 1.

.. image:: Banda_Arc_Region01.png
   :width: 80%

| **2. gmt makecpt -Crelief -T-6000/6000/200 -D -Z -H > elevation.cpt** to make color palette tables

``-Crelief`` specifies the input cpt to be `relief <http://soliton.vm.bytemark.co.uk/pub/cpt-city/gmt/GMT_relief.png>`_, click to see a full list of `built-in cpt <https://docs.generic-mapping-tools.org/latest/cookbook/cpts.html#of-colors-and-color-legends>`_

``-T-6000/6000/200`` defines the range of the new CPT by giving the lowest and highest z-values as -6000 and 6000, the increment is 200.

``-D`` selects the back- and foreground colors to match the colors for lowest and highest z-values in the output CPT. 

``-Z`` forces a continuous CPT when building from a list of colors and a list of z-values [discrete].

``-H`` is required for modern mode. 

``> elevation.cpt`` save the output CPT into a file named elevation.cpt

| **3. gmt grdimage @earth_relief_01m -Celevation.cpt -I+** to read a 2-D grid file and produce a colored map

``@earth_relief_01m`` will download global relief grids (the resolution is 1 minute, it depends on the map range) from the GMT server. Click to view a full list of provided `Global Relief Datasets <https://docs.generic-mapping-tools.org/latest/grdimage-classic.html?highlight=grdimage#global-relief-datasets>`_

``-Celevation.cpt`` specifies which CPT to use.

``-I+`` selects the default arguments to apply intensity. 

.. image:: Banda_Arc_Region02.png
   :width: 80%

| **4. gmt coast -W0.5p,black -Da** to add shorelines

``-W0.5p,black`` specifies the line width to be 0.5p (0.5 point) and line color to be black.

``-Da`` means that selecting the resolution of shorelines automaticly. 

.. image:: Banda_Arc_Region03.png
   :width: 80%

| **5. gmt inset begin -Dn1/0+jBR+w2.5c** to initiate an inset plotting

``-Dn1/0+jBR+w2.5c`` gives the location and size of the inset. Now the anchor point is relative to both main and inset map. In the main map, both x and y axes are normalzied with range to be 0-1. So here ``n1/0`` means the right most and lower most point, i.e., the bottom right point of the main map. In the inset map, the location of this anchor point is also at bottom right (BR). And the width of the inset map is 2.5c. 

| **6. gmt coast -Rg -JG123/-10/90/? -B -Swhite -A5000 -Ggray -W0.2p,black -Da --MAP_FRAME_PEN=0.2p** to plot continents and shorelines

``-Rg`` specifies the global domain.

``-JG123/-10/90/?`` specifies the projection type to be `orthographic azimuthal projection <https://docs.generic-mapping-tools.org/latest/cookbook/map-projections.html#jg>`_ and the center longitude and latitude to be 123 and -10. The horizon is 90 degree (<=90). The width is same as the inset map, thus use ?.

``-B`` means no ticks and gridlines.

``-Swhite`` specifies the color of wet areas to be white.

``-A5000`` means that an area smaller than 5000 km^2 will not be plotted. 

``-Ggray`` specifies the color of dry areas to be gray.

``--MAP_FRAME_PEN=0.2p`` sets the map's frame width to be 0.2p.

| **7. gmt inset end** to terminate the inset plotting

.. image:: Banda_Arc_Region04.png
   :width: 80%

| **8. gmt plot java_trench.txt -W1p,white** to plot trench locations

:download:`java_trench.txt <./java_trench.txt>` contains two columns of data, the first column is longitude and the second column is latitude. Each row means a sample point along the trench line. 

``-W1p,white`` specifies the line width and color to be 1p and white. 

| **9. echo '116 -12 Java trench' | gmt text -F+f8p,white** to add text

``116 -12`` specifies the location.

``Java trench`` is the text being added.

``-F+f8p,white`` specfies the fontsize and color of text. 

.. image:: Banda_Arc_Region05.png
   :width: 80%


| **10. awk 'NR>1 {print $5,$6}' GE_3_stations.txt | gmt plot -Si6p -W0.1p,black -Gcyan** to plot seismic stations

``Si6p`` specifies the symbols to be inverted triangles (i) and their size is 6p.

``-Gcyan`` specifies fill color of the symbols.

``-W0.1p,black`` specifies the outline properties of symbols.

| **11. awk -F"|" 'NR>3 {print $6,$5}' YS_30_stations.txt | gmt plot -Si6p -W0.1p,black -Gwhite** to plot more seismic stations

.. image:: Banda_Arc_Region06.png
   :width: 80%

| **12. gmt colorbar -Dn1/0+o0.5c/0c+jBL+w5.5c -Bxa3000 -By+l"Topo (m)" -Celevation.cpt** to add a color bar

``+o0.5c/0c`` means the anchor point in the main figure is further moved for 0.5c along the x direction.

``-By+l"Topo (m)"`` adds a label along the y axis.

.. image:: Banda_Arc_Region.png
   :width: 80%
