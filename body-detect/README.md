<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/img/logo.png" alt="mypy logo" width="300px"/>

EIH: Emergency Info Hub
=======================================

What is EIH?
-------------
Emergency Info Hub ([EIH](http://glasnost.itcarlow.ie/~softeng4/C00220135/index.html)),is a fourth year student project, has been designed to be a central website helps the emergency services to prepare for, respond to & recover from disaster, by providing all needed data for the targeted building (E.g. Number of people, area size and emergency exits).
The main objective of this project is giving the number of trapped people under rubbles or inside a building, by tracking their number using a simple movement sensor fitted on the main gate and face detection technology, and save this number to the cloud to be used when a disaster happens.

See [the documentation](http://glasnost.itcarlow.ie/~softeng4/C00220135/index.html#t3) for more detailes.

Hardware Requirements
------------
You need the list of hardware parts to be connected:

* Hardware List:
    * Raspberry Pi 4 with 8GB RAM && 8GB Memory Card
    * Raspberry Pi Camera 
    * IR Break Beam Sensor LEDs


Software Requirements
------------

1- You need Python 3.5 or later to run mypy.  You can have multiple Python
versions (2.x and 3.x) installed on the same system without problems.

In Ubuntu, Mint and Debian you can install Python 3 like this:

    $ sudo apt-get install python3 python3-pip

For other Linux flavors, macOS and Windows, packages are available at

  http://www.python.org/getit/


-- The file [setup.py](https://github.com/OAbouHajar/projectEIH/blob/master/body-detect/setup.py) is made to easy install all the requirements 
if you have Python 3 and pip3 installed on you device already, you can use the following command to setup the EIH project in fully. 
 
    $ python setup.py

file [setup.py](https://github.com/OAbouHajar/projectEIH/blob/master/body-detect/setup.py) support the following arguments to setup Google firebase URL:

* ["-db"] 
* ["--dburl"]

for example: 

    $ python setup.py -db https://<project-name>.firebaseio.com/<file-name>.json

Once you setup is completed you will have the follwing dependencies installed on your system.

* Dependencies:
    * Requests
    * python-firebase
    * python-opencv 
    * python-scipy 
    * ipython
    * firebase
    * imutils
    * python_jwt
    * gcloud
    * sseclient
    * parse
    * requests_toolbelt

