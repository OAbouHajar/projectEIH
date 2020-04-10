<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/img/logo.png" alt="mypy logo" width="150px"/>

EIH: Emergency Info Hub (Back-End)
=======================================

What is EIH?
-------------
Emergency Info Hub ([EIH](https://eih.pythonanywhere.com/)),is a fourth year student project, has been designed to be a central website helps the emergency services to prepare for, respond to & recover from disaster, by providing all needed data for the targeted building (E.g. Number of people, area size and emergency exits).
The main objective of this project is giving the number of trapped people under rubbles or inside a building, by tracking their number using a simple movement sensor fitted on the main gate and face detection technology, and save this number to the cloud to be used when a disaster happens.

See [the documentation](http://glasnost.itcarlow.ie/~softeng4/C00220135/index.html#t3) for more detailes.


Software Requirements
------------
To run the hardware part of EIH:
1- You need Python 3.5 or later to run mypy.  You can have multiple Python
versions (2.x and 3.x) installed on the same system without problems.

In Ubuntu, Mint and Debian you can install Python 3 like this:

    $ sudo apt-get install python3 python3-pip

For other Linux flavors, macOS and Windows, packages are available at

  http://www.python.org/getit/


-- The file [setup.py](https://github.com/OAbouHajar/projectEIH/blob/master/body-detect/setup.py) is made to easy install all the requirements 
if you have Python 3 and pip3 installed on you device already, you can use the following command to setup the EIH project in fully. 
 
    $ python setup.py

file [setup.py](https://github.com/OAbouHajar/projectEIH/blob/master/body-detect/setup.py) 

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
    * pyrebase

**Export the Environment Variables**
- once your setup.py done you have to set you environment variables to gain the access to you databese credentials:

    $ export FIREBASE_DB_URL=https://<'PROJECT-NAME'>.firebaseio.com/<'JSON-FILE-NAME'>.json
   
    $ export REG_BUILIDING_ID=<'THE-KEY-YOU-GET-AFTER-ADDING-THE-BUILDING-TO-THE-SYSTEM-FROM-THE-FRONT-END'>
   
    $ export DEVICE_ID=<'THE-DEVICE-ID-YOU-CHOSE'>
   
    $ export PROJECT_API_KEY=<'GOOGLE-FIREBASE-PRJECT-API-KEY'>


Hardware Requirements
------------
You need the list of hardware parts to be connected:

* Hardware List:
    * Raspberry Pi 4 with 8GB RAM && 8GB Memory Card
    * Raspberry Pi Camera 
    * IR Break Beam Sensor LEDs

Hardware Collaboration
------------

To have the best performance of your hardware the follwing instractions should be followed:

**IR Break Beam Sensor LEDs**
* Sensor one should be connected to GIPO 4 PIN(7)
* Sensor two should be connected to GIPO 17 PIN(11)
As it shown in the picture below:
<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/random/IR_connection.JPG" alt="mypy logo" width="600px"/>

* Both sensors should installed, on the both side of the door, with range [25cm] to [50cm] height from the ground taken the kids and adults height under considration as shown in the picture below:

<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/random/ir-collaboration.JPG" alt="mypy logo" width="600px"/>

**Raspberry Pi Camera**

* the camera connect to the camera port on the Raspberry Pi as it shown in the picture below.#

<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/random/cameraconnection.JPG" alt="mypy logo" width="600px"/>

* Now you need to enable camera support using the __raspi-config__ program you will have used when you first set up your Raspberry Pi:

    * Use the cursor keys to select and open Interfacing Options, and then select Camera and follow the prompt to enable the camera.
    * To test that the system is installed and working.

Try the following command:

    $ raspistill -v -o test.jpg


* The camera should be installed closer to the mid point of the entrance, with height range [190cm] to [220cm], with distance and an angle cover the full Entrance width and height.


<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/random/camera_sensor_setup.JPG" alt="mypy logo" width="600px"/>

How To Run EIH?
------------
To Run EIH Project you do need the same software package to both direction __IN__ or __OUT__ and that by telling the system what direction to run with the argument passed as the following commands:

### To Run The Project for [__OUT__] Direction ###

    $ python eihIR.py out

### To Run The Project for [__IN__] Direction ###

    $ python eihIR.py in

And this will change the calculations in the file [post-data-to-api.py](https://github.com/OAbouHajar/projectEIH/blob/master/body-detect/post-data-to-api.py) in the following code.

```javascript
if args["numberOUT"] is not None:
    // substact the number coming from the API to the number coming from the RassPi
    newNumber = preNumber- currentNumberOUT
elif args["numberIN"] is not None:
    // add the number coming from the API to the number coming from the RassPi
    newNumber = preNumber + currentNumberIN
```

***To Run the Project In The Both Direction, You need One Software Package and Two Hardware Set***
***As It's Shown In The Picture***


<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/random/in_and_out.JPG" alt="mypy logo" width="600px"/>


