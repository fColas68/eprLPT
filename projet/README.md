# Evaluation of scheduling algorithms

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Collaboration](#collaboration)

### General Info
***
![Image text](http://ctu.univ-fcomte.fr/sites/ctu/files/inline-images/SUP_final2020_nom.png)

#### Evaluation of scheduling algorithms.

The goal of this project is to evaluate and compare scheduling algorithms for the P||Cmax problem.  
First, job cost instances are either randomly generated according to distribution functions such as the uniform function, the gamma function, and the beta function, or retrieved from real job logs, from a Parallel Worklaod Archive. Then these instances are subjected to the LPT, SLACK, LDM and COMBINE algorithms.

#### project status

Documents || implementation
:----- | ----- | :-----
itsefl | : | **in progress**
user's manual | : | **in progress**
report | : | **in progress**
||
||

Algorithm || implementation
:----- | ----- | :-----
LPT | : | functional
SLACK | : | functional
LDM | : | **in progress**
COMBINE | : | **in progress**
||
||

instances generation || implementation | with seed management
:----- | ----- | :----- | :-----
uniform | : | functional | yes
non-uniform | : | functional | yes
lambda | : | functional | yes
beta | : | functional | yes
exponential | : | functional | yes
Parallel Workload Archive | : | functional | no
|||
|||

Module || implementation
:----- | ----- | :-----
result csv file export  | : | **in progress**
results statistics gui | : | **not started**

## Technologies
***
(in progress)  
A list of technologies used within the project:
* [Python](https://www.python.org/): Version 3.4 
* [pandas library](https://pandas.pydata.org/): Version 0.14.1-2
* [rStudio](https://rstudio.com/solutions/r-and-python/): Version xxx
## Installation
***
(in progress)  
The project is composed of PYTHON scripts. You just have to install them from github, as well as the modules they use.  
The installation procedure is given for a Linux environment using the APT package manager. you will have to adapt the installation commands to the target environment. And also, the paths and directories used must be modified if the scripts are executed under windows (replace the / characters in \\). see below.  

* installing the required modules

```
$ sudo apt-get install python3
```

* get the script from github

```
$ 
$ git clone 
$ cd ../path/
```

* adapt directory management to windows

## Usage
***
(in progress)  
open test.py with IDLE using Python 3, and run it.

## Collaboration
***
(in progress)  

