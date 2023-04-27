# W2-PD-Dict

Tested on Ubuntu 22.04.2 LTS.

## Installation Note

### Install the dependencies

```bash
sudo apt-get install cmake-qt-gui libboost-system-dev libpython3.10-dev libxt-dev libxcursor-dev libopengl-dev libgl1-mesa-dev
sudo apt install qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools qttools5-dev
sudo apt-get install libqt5x11extras5-dev libqt5svg5-dev qtxmlpatterns5-dev-tools
sudo apt install python3-sklearn
sudo apt install libsqlite3-dev
sudo apt install libeigen3-dev
sudo apt install gawk
sudo apt install git
```

### Install Paraview

First, go in the root of this repository and run the following commands:
(replace the `5` in `make -j 5` by the number of available cores on your system)

```bash
git clone https://github.com/topology-tool-kit/ttk-paraview.git
cd ttk-paraview
git checkout 5.10.0
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DPARAVIEW_USE_PYTHON=ON -DPARAVIEW_INSTALL_DEVELOPMENT_FILES=ON -DCMAKE_INSTALL_PREFIX=../install ..
make -j 5
make install -j 5
```
Some warnings are expected when using the `make` command, they should not cause any problems.

Stay in the build directory and set the environment variables:
(replace `3.10` in `python3.10` by your version of python)

```bash
PV_PREFIX=`pwd`/../install
export PATH=$PATH:$PV_PREFIX/bin
export LD_LIBRARY_PATH=$PV_PREFIX/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PV_PREFIX/lib/python3.10/site-packages
```

### Install TTK

Go in the `ttk-newMethodCompression` directory then run the following commands:
(replace the `5` in `make -j 5` by the number of available cores on your system)

```
mkdir build
cd build
paraviewPath=`pwd`/../../ttk-paraview/install/lib/cmake/paraview-5.9
cmake -DCMAKE_INSTALL_PREFIX=../install -DEigen3_DIR=/usr/share/eigen3/cmake -DParaView_DIR=$paraviewPath ..
make -j 5
make install -j 5
```

Stay in the build directory and set the environment variables:
(replace `3.10` in `python3.10` by your version of python)

```bash
TTK_PREFIX=`pwd`/../install
export PV_PLUGIN_PATH=$TTK_PREFIX/bin/plugins/TopologyToolKit
export LD_LIBRARY_PATH=$TTK_PREFIX/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH:$TTK_PREFIX/lib/python3.10/site-packages
```

### Get the result

Go in the root directory and then go in the `dataAndScripts` directory:

#### Table 1
There are two options, first to reproduce the fifth line of the fifth column you can run the following line:

```bash
python3 pythonScriptTestOneLine.py
```

To reproduce the whole fifth column you can run:

```bash
python3 pythonScriptParsingTest.py
```

Both of those scripts will ask you the number of threads allocated for the experiments when the following
sentence appears `Please chose the number of threads: ` type it and press enter.
Some warnings and "errors" from Paraview are expected, they do not cause any problems.
A time table will appear at the end in the terminal.
The outputs of the experiments (the dictionary and the weights) can be found in the `Outputs` directory
in a vtm format for the former and in a csv format for the latter.







