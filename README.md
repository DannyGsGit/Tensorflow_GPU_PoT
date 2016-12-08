# Python-TensorFlow-CUDA Environment Setup

This setup documents the configuration of a Python-TensorFlow-CUDA environment in Linux.

## System Configuration
This writeup was completed under the following system configuration:

* Hardware:
  * CPU: Dual Intel Xeon
  * GPU: NVIDIA GTX980
* OS: Ubuntu Server 14.04
* Python 3.4.3 (Ubuntu default)

## Virtual Environment Setup
We will use virtual environments to run TensorFlow. In this sample, we will put virtual environments in the `~/Python3/Environments` directory.

* We will first ensure all packages are up to date by running the following commands: </br>
```
$ sudo apt-get update
$ sudo apt-get updgrade
```
* Some versions of Ubuntu (i.e. 14.04) will not have *pyvenv* installed by default, so we will install *pyvenv* with the following: </br>
```
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

## (Optional) Add Rodeo IDE and dependencies
To simplify development of data science applications, we will use the Rodeo IDE. Using virtual environments requires minor configuration of Rodeo for operation inside the virtual environment.

* Install package dependencies required for Rodeo: </br>
