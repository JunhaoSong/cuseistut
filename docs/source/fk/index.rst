FK & CAP Installation Guide
===========================

These instructions are adapted from:

https://seiswave.cn/oh-my-cap/install/

https://cuseistut.readthedocs.io/en/latest/gcap/index.html#/

===============
1. Package required
===============

Compilers & build tools: gcc, gfortran, make

Seismic tools: rdseed, SAC, TauP, FK, gCAP

Plotting: GMT6


===============
2. Installation
===============

2.1 Compile tools

*2.1.1 MacOS*

Install Homebrew

.. code-block::
    :linenos:
 
    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    $ brew install gcc gfortran make

*2.1.2 Linux*

.. code-block::
    :linenos:
    
    $ sudo apt-get install gcc gfortran

2.2 rdseed

rdseed :download:`rdseedv5.3.1.tar.gz <./rdseedv5.3.1.tar.gz>`  is used to convert SEED files to SAC format

Reference: https://blog.seisman.info/rdseed-install/

.. code-block::
    :linenos:
    
    $ tar -xvf rdseedv5.3.1.tar.gz
    $ mkdir ~/opt
    $ mv rdseedv5.3.1 ~/opt
    $ cd ~/opt/rdseedv5.3.1

    #For MacOS, run following lines 
    $ ./rdseed.mac.x86_64
    $ xattr -d com.apple.quarantine rdseed.mac.x86_64
    $ mv rdseed.mac.x86_64 rdseed
    $ echo 'export PATH=${HOME}/opt/rdseedv5.3.1:${PATH}'>> ~/.zshrc

    #For Linux, run following lines
    $ ./rdseed.rh6.linux_64
    $ mv rdseed.rh6.linux_64 rdseed
    $ echo 'export PATH=${HOME}/opt/rdseedv5.3.1:${PATH}'>> ~/.bashrc

2.3 SAC

SAC is used to process sac file

Reference: 

https://seisman.github.io/SAC_Docs_zh/install/

You need to download the package by yourself using following link:

http://ds.iris.edu/ds/nodes/dmc/forms/sac/


*2.3.1 MacOS*

.. code-block::
    :linenos:
    
    $ xcode-select --install
    $ brew install --cask xquartz
    $ tar -xvf sac-102.0-mac.tar.gz
    $ sudo mv sac /usr/local
    #Add environment variables:
    $ echo 'export SACHOME=/usr/local/sac' >> ~/.zshrc
    $ echo 'export SACAUX=${SACHOME}/aux' >> ~/.zshrc
    $ echo 'export PATH=${SACHOME}/bin:${PATH}' >> ~/.zshrc
    $ echo 'export SAC_DISPLAY_COPYRIGHT=1' >> ~/.zshrc
    $ echo 'export SAC_PPK_LARGE_CROSSHAIRS=1' >> ~/.zshrc
    $ echo 'export SAC_USE_DATABASE=0' >> ~/.zshrc
    $ source ~/.zshrc
    $ sac

*2.3.2 Linux*

.. code-block::
    :linenos:

    $ sudo apt update
    $ sudo apt install libc6 libsm6 libice6 libxpm4 libx11-6
    $ sudo apt install zlib1g libncurses6
    $ tar -xvf sac-102.0-linux_x86_64.tar.gz 
    $ sudo mv sac /usr/local 
    #Add environment variables:
    $ echo 'export SACHOME=/usr/local/sac' >> ~/.bashrc
    $ echo 'export SACAUX=${SACHOME}/aux' >> ~/.bashrc
    $ echo 'export PATH=${SACHOME}/bin:${PATH}' >> ~/.bashrc
    $ echo 'export SAC_DISPLAY_COPYRIGHT=1' >> ~/.bashrc
    $ echo 'export SAC_PPK_LARGE_CROSSHAIRS=1' >> ~/.bashrc
    $ echo 'export SAC_USE_DATABASE=0' >> ~/.bashrc
    $ source ~/.bashrc
    $ sac

2.4 GMT6

GMT is used for high-quality plotting

Reference: https://docs.gmt-china.org/latest/install/

*2.4.1 MacOS*

.. code-block::
    :linenos:

    $ brew update && brew upgrade
    $ brew install gmt
    $ brew install ghostscript
    $ brew install graphicsmagick
    $ brew install ffmpeg
    $ gmt --version

*2.4.2 Linux*

.. code-block::
    :linenos:

    $ sudo apt update
    $ sudo apt install gmt gmt-dcw gmt-gshhg
    $ sudo apt install xdg-utils
    $ sudo apt install gdal-bin
    $ sudo apt install ghostscript
    $ sudo apt install graphicsmagick
    $ sudo apt install ffmpeg
    $ gmt --version

If the version is not GMT6, see: https://docs.gmt-china.org/latest/install/conda/

2.5 TauP

TauP  :download:`TauP-2.6.1.tgz <./TauP-2.6.1.tgz>` is used to calculate theoretical ray paths and arrival times

Reference: https://seismo-learn.org/software/taup/install/

For MacOS, run following lines to install JAVA

.. code-block::
    :linenos:

    $ brew install openjdk
    $ sudo ln -sfn $(brew --prefix)/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

For Linux, run following lines to install JAVA

.. code-block::
    :linenos:

    $ sudo apt install default-jdk
    $ java -version

.. code-block::
    :linenos:

    $ wget http://www.seis.sc.edu/downloads/TauP/TauP-2.6.1.tgz
    $ tar -xvf TauP-2.6.1.tgz
    $ mkdir -p ~/opt/
    $ mv TauP-2.6.1 ~/opt/

For MacOS, run following lines

.. code-block::
    :linenos:

    $ echo 'export PATH=${HOME}/opt/TauP-2.6.1/bin:${PATH}' >> ~/.zshrc
    $ source ~/.zshrc
    $ taup

For Linux, run following lines

.. code-block::
    :linenos:

    $ echo 'export PATH=${HOME}/opt/TauP-2.6.1/bin:${PATH}' >> ~/.bashrc
    $ source ~/.bashrc
    $ taup

2.6 FK

FK computes synthetic Green’s functions for layered velocity models written by Prof. Lupei ZHU 

Source: 

http://www.eas.slu.edu/People/LZhu/downloads/fk3.3.tar/

https://seismo-learn.org/software/fk/install/

We recommend using oh-my-cap (simpler on macOS):

https://seiswave.cn/oh-my-cap/install/

.. code-block::
    :linenos:

    $ wget https://github.com/wangliang1989/oh-my-cap/archive/v2.0.0.tar.gz
    $ tar -zxvf v2.0.0.tar.gz
    $ mv oh-my-cap-2.0.0 ~/opt/
    $ cd ~/opt/oh-my-cap/src/fk
    $ make

For MacOS, run the following line

.. code-block::
    :linenos:

    $ echo 'export PATH=${HOME}/opt/oh-my-cap-2.0.0/src/fk:${PATH}' >> ~/.zshrc
    $ source ~/.zshrc
    $ fk.pl

For Linux, run the following line

.. code-block::
    :linenos:

    $ echo 'export PATH=${HOME}/opt/oh-my-cap-2.0.0/src/fk:${PATH}' >> ~/.bashrc
    $ source ~/.bashrc
    $ fk.pl

2.7 CAP

CAP is a focal-mechanism inversion method developed by Prof. Lupei ZHU.

Source:

http://www.eas.slu.edu/People/LZhu/downloads/gcap1.0.tar/

https://blog.seisman.info/gcap-install/

We recommend using oh-my-cap (simpler on macOS):

https://seiswave.cn/oh-my-cap/install/

.. code-block::
    :linenos:

    $ cd ~/opt/oh-my-cap/src/gcap
    $ make

For MacOS, run following lines

.. code-block::
    :linenos:

    $ echo 'export OH_MY_CAP=${HOME}/opt/oh-my-cap-2.0.0' >>  ~/.zshrc
    $ echo 'export PATH=${HOME}/opt/oh-my-cap-2.0.0/src/gcap:${PATH}' >> ~/.zshrc
    $ source ~/.zshrc
    $ cap.pl

For Linux, run following lines

.. code-block::
    :linenos:

    $ echo 'export OH_MY_CAP=${HOME}/opt/oh-my-cap-2.0.0' >>  ~/.bashrc
    $ echo 'export PATH=${HOME}/opt/oh-my-cap-2.0.0/src/gcap:${PATH}' >> ~/.bashrc
    $ source ~/.bashrc
    $ cap.pl


===============
3. Run an example
===============

3.1 Calculate Green’s function (FK)

.. code-block::
    :linenos:

    $ cd ~/opt/oh-my-cap Glib
    $ perl run_fk.pl model.fk

3.2 Data pre-processing

.. code-block::
    :linenos:

    $ cd ../example/
    $ perl process.pl 20080418093658

3.3 Inversion (CAP)

.. code-block::
    :linenos:
    
    $ perl weight.pl 20080418093658
    $ perl inversion.pl 20080418093658
    $ perl gmt6depth.pl 20080418093658
    $ perl depth.pl 20080418093658


===============
4. Optional: Install pyfk
===============
 
Reference: https://github.com/ziyixi/pyfk/blob/master/docs/introduction/install.rst/

.. code-block::
    :linenos:

    $ conda create -n fk python=3.9 -y
    $ conda activate fk
    $ conda install -c conda-forge -y  numpy=1.26 "cython<3" setuptools wheel scipy make notebook

For MacOS, run following lines

.. code-block::
    :linenos:

    $ pip install cysignals pyfk --no-build-isolation
    $ jupyter notebook

For Linux, run following lines

.. code-block::
    :linenos:
    
    $ pip install cysignals pyfk
    $ jupyter notebook

Open and run pyfk.ipynb :download:`./pyfk.ipynb <./pyfk.ipynb>`

This notebook was written by Khalil and revised by Qili

The test systems are macOS 15.6.1 and Ubuntu 18.04.6

