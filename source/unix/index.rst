Unix commands
#############

The tutorial is based on the Unix system. In this chapter, we will introduce some basic Unix commands that are useful in later modules. We will introduce basic commands related to Directory management, text file reading, Unix input and output redirection, and the Pipe command. the file used in this tutorial is the earthquake catalog and station list in the Banda Arc–Australian Plate Collision Zone (Jiang et al., 2022).

Developed by Po Wang LAM (Ryan) under the instruction of Han CHEN.

============
1 Target
============
Master the basic operation in the directory and file.  

Understanding the input and output redirection and the Pipe command. 

Make sub-catalogs and sub-station lists based on the Downloaded complete earthquake catalog and save the file in corresponding directories.

==================================
2 Commands and concept included
==================================
Directory management:  :file:`pwd` :file:`cd` :file:`mkdir` :file:`ls`

File reading: :file:`more` :file:`cat` :file:`wc` :file:`grep` :file:`awk`

Input and output redirection: :file:`>` :file:`<`

Pipe: :file:`|`

=============================== 
3 Commands usage and examples
===============================
3.1 Directory management
========================
Before any operation, it is important to make sure you are at the correct working directory. First, to know which directory you are at, you can use the print working directory command :file:`pwd`. It will print the current working directory as output in the terminal.

.. code-block::
    :linenos:
	
    $ pwd
    /current-directory     #for illustration only

You are now at :file:`current-directory`. Then, you should change the current directory to the work directory you want, here we used the desktop as example, by the command change directory :file:`cd`. 

.. code-block::
    :linenos:
	
    $ cd /home/user/desktop
    $ pwd
    /home/user/desktop
    
.. note::

    The :file:`/home/user/desktop` here is used as an example. please change it to your own directory accordingly.

Now you are at the  :file:`/home/user/desktop`. Before downloading the data, you may want to create an own directory for storing them. This can be done by a simple command :file:`mkdir`.

.. code-block::
    :linenos:
	
    $ mkdir data_storage
    
The command  :file:`ls` list the content under current directory. Now run the list files :file:`ls` command the make sure the  :file:`Data_storage` is created. 

.. code-block::
    :linenos:
	
    $ mkdir ls
    Data_storage
    
Now you can change your working directory to :file:`Data_storage`. 

.. code-block::
    :linenos:
	
    $ cd Data_storage
    $ ls
    
After running the :file:`ls`, no output was shown, which means that the directory is now empty.

    
.. Tip::

    Several common commands for dealing with directories
    
    ls（list files）: List directories and file names
    
    cd（change directory）：Switch directory
    
    pwd（print work directory）：Show current directory
    
    mkdir（make directory）：Create a new directory
    
    rmdir（remove directory）：Delete an empty directory
    
    cp（copy file）: Copy a file or directory
    
    rm（remove）: delete file or directory
    
    mv（move file）: Move files and directories, or change the names of files and directories

3.2 File reading
===================
3.2.1 Browse documents
-----------------------
Now we can download the catalog file. The file could be download from :download:`here <./Unix_command_Materials.tgz>`. After downloading the catalogue, it will first be stored in the :file:`~/Downloads`. To move the files from :file:`~/Downloads` to the directory you created, you may use the command  :file:`mv`

.. code-block:: 
    :linenos:
	
    $ pwd
    Home/user/desktop/Data_storage
    $ mv ~/Downloads/Unix_command_Materials.tgz ./
    $ ls
    Unix_command_Materials.tgz
    
.. note::

    The directory :file:`~/Downloads` here is suitable for Unix system. please change it to your own directory accordingly.

The file was now moved to your working directory. As the file is zipped as a .tgz file, it needs to be unzipped. It can be done by the command :file:`tar`

.. code-block:: 
    :linenos:
	
    $ tar -zxf Unix_command_Materials.tgz
    $ ls
    CUSeisTut Unix_command_Materials.tgz
    
The file was now unzipped and the directory :file:`CUSeisTut` was create. Change your working directory to the :file:`CUSeisTut`  and use  :file:`ls` to check the contents.

.. code-block:: 
    :linenos:
	
    $ cd CUSeisTut
    $ ls
    A_Detailed_EQ_Catalog  Stations_Info  TSR_Paper 
    $ ls A_Detailed_EQ_Catalog
    banda_arc_catalog.txt
    $ ls Stations_Info TSR_Paper
    GE_3_stations.txt  YS_30_stations.txt
    Stations_Info:
    GE_3_stations.txt  YS_30_stations.txt

    TSR_Paper:
    tsr-2021041.1.pdf  tsr-2021041_supplement.docx

We will first look at the earthquake catalog :file:`banda_arc_catalog.txt` stored in :file:`A_Detailed_EQ_Catalog`, try to change your working directory to there. 

Before processing the file, we would like to ensure the file is compatible and contains the desired data. There are several ways for reading a text file from the terminal, we would like to introduce two methods:   :file:`more`   :file:`cat`

.. code-block:: 
    :linenos:
	
    $ cd A_Detailed_EQ_Catalog
    $ ls
    banda_arc_catalog.txt
    $ more banda_arc_catalog.txt
     indx year mon day time sec_relative_to_day  res      lat     lon    dep    mag  visual_flag hypodd_flag
       2 2014 03 18 16:56:34.260000 60994.2600    0.697   -9.092  124.191   82.1   3.1 1 1
       3 2014 03 19 14:39:17.472600 52757.4726    1.593   -8.519  126.329   23.2   3.0 1 0
       4 2014 03 20 15:32:39.914100 55959.9141    0.706   -7.482  127.900  192.6   3.7 1 0
       5 2014 03 21 15:10:35.760000 54635.7600    1.090   -8.936  124.325   81.2   1.6 1 1
       6 2014 03 21 18:16:37.720199 65797.7202    1.898   -8.928  125.775   69.8   2.3 1 0
       7 2014 03 22 08:18:17.449799 29897.4498    1.095   -8.974  125.587   -4.5   3.0 1 0
       8 2014 03 22 13:57:21.227599 50241.2276    0.792   -9.891  123.950   62.9   3.9 1 0
       9 2014 03 22 15:43:47.217700 56627.2177    1.546   -8.747  122.528  114.1   2.4 1 0
      10 2014 03 22 19:23:44.019000 69824.0190    0.642   -7.383  128.098  218.4   2.9 1 0
      11 2014 03 23 04:37:50.889999 16670.8900    0.787   -9.359  124.140   57.7   3.3 1 1
      12 2014 03 23 12:16:37.705200 44197.7052    1.017  -10.549  123.603   -4.1   3.3 1 0
      13 2014 03 24 15:56:41.793600 57401.7936    1.512   -7.118  127.153  152.0   3.0 1 0
      14 2014 03 24 17:16:01.760000 62161.7600    1.904   -9.108  124.246   68.7   3.1 1 1
      17 2014 03 25 17:14:15.798098 62055.7981    0.768   -7.407  126.617  199.0   2.5 1 0
      18 2014 03 25 18:57:23.260000 68243.2600    0.606   -9.000  124.130   75.6   1.8 1 1
      19 2014 03 26 06:32:57.887500 23577.8875    0.851   -7.449  127.497  166.7   2.6 1 0
      23 2014 03 29 20:31:47.700000 73907.7000    0.734   -9.381  123.590   82.9   3.0 1 1
      24 2014 03 31 10:56:15.241300 39375.2413    0.973   -7.424  126.049   23.6   4.1 1 0
      26 2014 04 01 01:00:36.254898  3636.2549    0.932   -7.614  127.268  188.9   2.9 1 0
      27 2014 04 02 03:01:25.829400 10885.8294    1.684   -7.507  122.368   21.8   4.4 1 0
      28 2014 04 02 15:26:23.424199 55583.4242    0.827   -9.073  124.145   37.0   2.4 1 0
      29 2014 04 02 18:20:08.600000 66008.6000    0.840   -8.897  124.130   78.2   2.2 1 1
      30 2014 04 02 19:06:23.708500 68783.7085    1.137   -9.317  120.447  131.6   3.3 1 0
      31 2014 04 03 11:44:25.794800 42265.7948    0.842   -7.779  128.245  218.4   3.5 1 0
      33 2014 04 04 07:06:34.235300 25594.2353    1.358   -7.970  123.634  119.6   3.6 1 0
      34 2014 04 04 11:18:03.472600 40683.4726    0.769   -8.941  124.175   14.9   2.4 1 0
      35 2014 04 04 16:50:22.464900 60622.4649    2.933   -8.011  127.448  115.0   2.2 1 0
      36 2014 04 05 02:37:26.165300  9446.1653    1.564   -8.899  125.963   -4.5   2.4 1 0
      --More--(0%)

The :file:`more` command outputs the first few rows of the file, we can press “Enter” to show more lines. and Press 'Ctrl+C' to exit the command.

.. code-block:: 
    :linenos:

    $ cat banda_arc_catalog.txt
       ......
       28683 2018 12 29 12:28:05.790000 44885.7900    0.860   -8.220  123.825  180.2   3.5 1 1
       28684 2018 12 29 15:32:39.982800 55959.9828    1.553   -8.846  124.025   66.1   2.0 1 0
       28686 2018 12 29 20:29:02.320000 73742.3200    0.652  -10.036  123.314   31.6   2.3 1 1
       28688 2018 12 30 03:43:30.899300 13410.8993    1.217   -7.994  128.068  183.4   3.7 1 0
       28689 2018 12 30 04:10:53.381499 15053.3815    1.544   -9.896  118.925   33.8   5.0 1 0
       28692 2018 12 30 14:47:19.025200 53239.0252    0.865   -7.788  127.986  176.9   3.5 1 0
       28695 2018 12 30 18:21:30.339600 66090.3396    0.942   -9.970  123.299   60.6   2.6 1 0
       28696 2018 12 30 20:22:25.646099 73345.6461    0.928   -8.069  123.234  206.4   3.2 1 0
       28697 2018 12 31 04:36:34.280000 16594.2800    0.769   -8.808  124.321   96.4   2.5 1 1
       28699 2018 12 31 19:13:00.751600 69180.7516    0.983   -8.879  123.539    5.2   2.9 1 0


The :file:`cat` command will pop the whole content at once.


We could count the total lines and characters of the catalog by using the :file:`wc` command.

.. code-block:: 
    :linenos:
	
    $ wc -l banda_arc_catalog.txt
    19075 banda_arc_catalog.txt
    $ wc -c banda_arc_catalog.txt
    1735843 banda_arc_catalog.txt

The parameters :file:`-l` and :file:`-c` are parameters that choose the output. :file:`-l` means count the lines of the file and :file:`-c` means count the total characters of the file. The catalog is a very large catalog with 19074 events (first line of the file indicates the contents).

.. tip::
    The :file:`$?` could be used to represent specific column, such as :file:`$1` represents the 1st culumn, :file:`$2` represents the 2nd column, :file:`$NF` represents the last column.
    

After viewing the original catalog, some processes can be done to divide the catalog for the analysis. The target is to generate sub-divided catalogs based on different properties like time and magnitude. To achieve this, some operational commands need to be used. :file:`grep` and :file:`awk` is two simple commands for searching certain content from the file.

3.2.1 Extract the text content
-------------------------------

The :file:`grep` is a command used to search for texts and strings. It output all the rows that contain the searched character.

For example, when we would like to search earthquakes that occurred in 2014, we can use the following commands.

.. code-block:: 
    :linenos:
	
    $ grep ‘2014’ banda_arc_catalog.txt
      …
      2707 2014 12 31 13:46:44.510000 49604.5100    1.210   -8.959  123.953   91.9   3.2 1 1
      2709 2014 12 31 15:50:22.129999 57022.1300    0.599   -8.116  120.694    3.2   2.1 1 1
      2710 2014 12 31 15:53:45.350000 57225.3500    1.305   -9.457  119.644   64.3   2.2 1 1
      2711 2014 12 31 16:22:48.430000 58968.4300    1.488   -9.476  120.123   75.6   1.9 1 1
      2712 2014 12 31 18:16:21.280000 65781.2800    1.329  -10.439  123.626  110.1   2.4 1 1
      2714 2014 12 31 19:07:44.320000 68864.3200    1.350   -9.601  119.909   55.2   1.8 1 1
      2715 2014 12 31 19:14:17.627898 69257.6279    1.265   -9.331  124.087    4.9   2.5 1 0
      2716 2014 12 31 19:19:49.720000 69589.7200    1.649   -9.662  119.824   24.4   1.9 1 1
      2717 2014 12 31 19:47:27.840000 71247.8400    1.068   -9.146  118.864   51.9   2.6 1 1
      2718 2014 12 31 20:24:31.120000 73471.1200    1.724   -9.072  123.987   73.2   1.9 1 1
      2720 2014 12 31 20:33:22.680000 74002.6800    1.350   -8.293  120.601   39.5   2.1 1 1
      2721 2014 12 31 20:40:36.260000 74436.2600    0.917  -10.070  119.152   13.2   2.2 1 1
      2722 2014 12 31 22:46:19.320000 81979.3200    1.516   -9.511  120.082   70.5   1.9 1 1
      6638 2015 05 07 06:06:54.990000 22014.9900    0.837   -9.458  125.033    7.5   2.7 1 1
      6771 2015 05 12 06:06:54.222800 22014.2228    0.684   -8.800  120.459  109.0   2.1 1 0
     12014 2015 11 04 19:28:46.320000 70126.3200    1.223   -8.298  125.076    5.2   2.4 1 1
     20141 2016 06 18 18:32:52.840000 66772.8400    0.836   -8.311  123.929  176.8   1.9 1 1
     20142 2016 06 18 19:14:26.900000 69266.9000    1.531   -9.441  124.789    4.1   1.8 1 1
     20143 2016 06 18 20:03:26.445700 72206.4457    2.369   -8.408  126.589   -3.2   2.6 1 0
     20144 2016 06 18 20:31:17.911600 73877.9116    1.388   -8.957  119.781   21.3   2.0 1 0
     20147 2016 06 19 01:38:58.808900  5938.8089    1.081  -11.094  118.986  110.4   3.2 1 0
     20148 2016 06 19 05:31:08.009999 19868.0100    1.257   -9.681  119.794   56.3   2.3 1 1
     22014 2016 09 11 08:59:33.940000 32373.9400    1.514   -8.672  118.465  119.5   2.6 1 1
     27150 2018 07 25 10:21:49.201498 37309.2015    0.947   -8.532  126.669   69.8   3.4 1 0

The command gives an output in the terminal with all rows including ‘2014’. But here are some problem, some row contains '2014', but the '2014' does not represent the year 2014 (e.g., line 16 to line 26).

The :file:`awk` is a more powerful tool for manipulating data and producing reports. The awk command allows the user to use variables, numeric functions, string functions, and logical operators.

.. tip::
    General command: awk [‘pattern  {action}’]  [file_name]
    
    [pattern] : indicate where to execute the action, for example, NR>10 means lines > 10

    [action] : the default action is to print out all lines fulfilled the pattern, but the action can also be more specific with different input like calculation.

    [file_name] : the file to process
    
    The :file:`-F` parameter could be used to specify the delimiter. such as :file:`awk -F "[|]" [‘pattern  {action}’]  [file_name]` specify the :file:`|` as the delimiter. By default, the delimiter is :file:`Space`.

.. code-block::
    :linenos:

    $ awk 'NR<20{if ($11>3.0) print;}' banda_arc_catalog.txt
     indx year mon day time sec_relative_to_day  res      lat     lon    dep    mag  visual_flag hypodd_flag
       2 2014 03 18 16:56:34.260000 60994.2600    0.697   -9.092  124.191   82.1   3.1 1 1
       4 2014 03 20 15:32:39.914100 55959.9141    0.706   -7.482  127.900  192.6   3.7 1 0
       8 2014 03 22 13:57:21.227599 50241.2276    0.792   -9.891  123.950   62.9   3.9 1 0
      11 2014 03 23 04:37:50.889999 16670.8900    0.787   -9.359  124.140   57.7   3.3 1 1
      12 2014 03 23 12:16:37.705200 44197.7052    1.017  -10.549  123.603   -4.1   3.3 1 0
      14 2014 03 24 17:16:01.760000 62161.7600    1.904   -9.108  124.246   68.7   3.1 1 1
      24 2014 03 31 10:56:15.241300 39375.2413    0.973   -7.424  126.049   23.6   4.1 1 0


In this example, the pattern is :file:`NR>20` and the action is :file:`if($11>3.0) print`. In a readable way, it means for the first 20 lines, print all rows where their column 11($11) is larger than 3.0. With the physical meaning of each column, the output is all events with a magnitude over 3 within the first 19 events

We could print the column that we are interested in separately by adding the column index after :file:`print`.

.. code-block::
    :linenos:
    
    $ awk 'NR<20{if ($11>3.0) print $1,$2,$3,$4,$5,$8,$9,$10;}' banda_arc_catalog.txt
    indx year mon day time lat lon dep
    2 2014 03 18 16:56:34.260000 -9.092 124.191 82.1
    4 2014 03 20 15:32:39.914100 -7.482 127.900 192.6
    8 2014 03 22 13:57:21.227599 -9.891 123.950 62.9
    11 2014 03 23 04:37:50.889999 -9.359 124.140 57.7
    12 2014 03 23 12:16:37.705200 -10.549 123.603 -4.1
    14 2014 03 24 17:16:01.760000 -9.108 124.246 68.7
    24 2014 03 31 10:56:15.241300 -7.424 126.049 23.6

3.3 File output and input
=========================
:file:`>` and :file:`<` is the Output and Input Redirection in Unix. Most Unix system commands take input from your terminal and send the resulting output back to your terminal, as what shown in above examples.

If the notation :file:`> file`  is appended to any command, the output of that command will be written to the file instead of your terminal.

.. code-block::
    :linenos:
    
    $ echo "hello word"
    hello word
    $echo "hello world" > test.txt
    cat test.txt
    hello word
    
In the second command, :file:`>` was appended to the echo command, so the output was written to the file 'test.txt' rather than the terminal.

.. Note::

    :file:`echo`: output the original content to the screen if it has no special meaning; if the output content has a special meaning, the output will print its meaning.

    :file:`>` will generate a new file if the file does not exist and will write over the file if the file already exists!
    
.. Note::
    
    Types of Redirection 

    1. Overwrite  

    :file:`>` standard output, :file:`<` standard input

    2. Appends  

    :file:`>>` standard output, :file:`<<` standard input

We could now use :file:`awk` to extract the earthquake based on various criterion and save the output as sub-catalog by using :file:`>`.

.. code-block::
    :linenos:

    $ mkdir earthquake-2014
    $ awk '{if ($2==2014) print;}' banda_arc_catalog.txt > earthquake-2014/banda_arc_catalog-2014.txt
    $ cd earthquake-2014
    $ ls
    banda_arc_catalog-2014.txt
    $ wc -l banda_arc_catalog-2014.txt
    1871 banda_arc_catalog-2014.txt
    
Here we make a directory :file:`earthquake-2014` and extract the earthquakes that occurred in 2014 (e.g. $2==2014) and save the sub-catalog into file 'banda_arc_catalog-2014.txt' under the directory. We than count the events number by using :file:`wc -l`
    

:file:`<` will direct the file as a standard input to the command, for example

.. code-block::
    :linenos:
    
    $ echo line1 > test.txt
    $ echo line2 >> test.txt 
    $ while read line
    $ do
    $ echo $line
    $ done < test.txt
    line1
    line2

Here we use :file:`<` to direct the file :file:`test.txt` as a standard input for the command :file:`while read line`. the command will read the file line by line as :file:`$line`. 

3.4 The Pipe in Unix
======================

Pipe is used to redirect the output of a command as the input another command

.. code-block::
    :linenos:

    $ grep 2014 banda_arc_catalog.txt | wc -l
    1882
    $ awk '{if ($2==2014) print;}' banda_arc_catalog.txt | wc -l 
    1871

In this example, we used the pipe :file:`|` to redirect the output of a command :file:`grep` and :file:`awk` as the input of command :file:`wc -l`. 

============
4 Exercise
============

4.1. Make a directory :file:`earthquake-Mag` under :file:`A_Detailed_EQ_Catalog`. Extract the year, mon, day, time, lat, lon, dep, and mag of earthquakes with Magnitude between 4 to 6 and save the output to file :file:`earthquake-Mag-4-6.txt`. Count the number of the extracted earthquakes.

4.2. Make a station list file with only station 'ALRB' and save it as :file:`Substation.lst` . Only Network, station, latitude, longitude, elevation are needed. Append same information of station 'PPLA' to the Subastaion.lst. 

============
References
============
Jiang C, Zhang P, White M C A, et al. A Detailed Earthquake Catalog for Banda Arc–Australian Plate Collision Zone Using Machine‐Learning Phase Picker and an Automated Workflow[J]. The Seismic Record, 2022, 2(1): 1-10.

