# Python-TensorFlow-CUDA Environment Setup

This setup documents the configuration of a Python-TensorFlow-CUDA environment in Linux.

## System Configuration
This writeup was completed under the following system configuration:

* Hardware:
  * CPU: Dual Intel Xeon
  * GPU: NVIDIA GTX980
* OS: Ubuntu Server 14.04
* Python 3.4.3 (Ubuntu default)

## System dependencies
```
$ sudo apt-get install build-essential python-dev
$ sudo apt-get install gfortran
$ sudo apt-get install swig
$ sudo apt-get install libatlas-dev
$ sudo apt-get install liblapack-dev
$ sudo apt-get install libfreetype6 libfreetype6-dev
$ sudo apt-get install libxft-dev
$ sudo apt-get install graphviz libgraphviz-dev
$ sudo apt-get install pandoc
$ sudo apt-get install libxml2-dev libxslt-dev zlib1g-dev
```

## Virtual Environment Setup
We will use virtual environments to run TensorFlow. In this sample, we will put virtual environments in the `~/Python3/Environments` directory.

* We will first ensure all packages are up to date by running the following commands: </br>
```
$ sudo apt-get update
$ sudo apt-get updgrade
```
* Some versions of Ubuntu (i.e. 14.04) will not have *pyvenv* and *pip* installed by default, so we will install them with the following: </br>
```
$ sudo apt-get install python3-pip
$ sudo apt-get install python3.4-venv
```
* Next, create the virtual environment with: </br>
```
$ python3 -m venv tensorflow_env
```
* Activate the environment by navigating to the *bin* directory of the new environment, then executing the activate script: </br>
```
$ cd ~/Python3/Environments/tensorflow_env/bin/
$ source activate
```
> To exit the virtual environment, simply type `deactivate` into the console.

## (Optional) Add Rodeo IDE
This section will install the Rodeo IDE and configure it to run in our venv.

* Activate the venv and install dependencies: </br>
```
$ cd ~/Python3/Environments/tensorflow_env/bin/
$ source activate
$ pip3 install jupyter-client
$ pip3 install ipykernel
$ pip3 install numpy
$ pip3 install pandas
$ pip3 install matplotlib
```

* Get the Rodeo deb file and install it: </br>
```
$ cd ///usr/local/bin/
$ sudo wget -O rodeo.deb https://www.yhat.com/products/rodeo/downloads/linux_64
$ sudo dpkg -i rodeo.deb
$ sudo apt-get install rodeo
```
> Some errors may be displayed during the installation, however have a look at whether Rodeo installed.

* When starting up Rodeo for the first time, you may encounter errors. Ignore the error message and click "Skip Startup"
* Inside Rodeo, navigate to *Rodeo > Preferences > Python* and set the *Python Path* to the python3 file in your virtual environment's `/bin` subdirectory.

## Install CUDA Toolkit & cuDNN

> TensorFlow requires an NVIDIA GPU with compute capability >3.0 per NVIDIA's compute table: https://developer.nvidia.com/cuda-gpus

In order to run TensorFlow, we must install CUDA Toolkit V7.0 (or later) and cuDNN 3.0 (or later). The packages are available here: https://developer.nvidia.com/cuda-downloads.

> Note that the CUDA installation is done at the system level, not inside the virutal environment.

* For this example, we download the .deb CUDA installer and place the file in the */usr/local/cuda* directory.
* In the terminal, navigate to the directory where CUDA was downloaded and execute the following commands to install: </br>
```
$ sudo dpkg -i cuda-repo-ubuntu1404-8-0-local_8.0.44-1_amd64.deb
$ sudo apt-get update
$ sudo apt-get install cuda
```

Next, we will install cuDNN. The files are located here: https://developer.nvidia.com/cudnn
* Download the cuDNN tarball appropriate for your OS and CUDA toolkit version.
* Extract the tarball and copy the file into the CUDA folder with the following: </br>
```
$ sudo tar -xvf cudnn-8.0-linux-x64-v5.1-rc.tgz -C /usr/local
```

## Install TensorFlow GPU Configuration
TensorFlow is available in both CPU-only and GPU-enabled versions. Here we will install the GPU-enabled version.
* Activate the virutal environment: </br>
```
$ cd ~/Python34/Environments/tensorflow_env/bin
$ source activate
```
* Install TensorFlow GPU-enabled: </br>
```
(tensorflow_env) $ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.0rc0-cp34-cp34m-linux_x86_64.whl
(tensorflow_env) $ pip3 install --upgrade $TF_BINARY_URL
```

## Enable GPU support

## Sources:
NVIDIA TensorFlow CUDA Installation Instructions. http://www.nvidia.com/object/gpu-accelerated-applications-tensorflow-installation.html#sthash.oP4cRwjF.dpuf
