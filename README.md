<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/img/logo.png" alt="mypy logo" width="150px"/>

EIH: Emergency Info Hub 
=======================================

The project link: https://www.e-hub.ie/

What is EIH?
-------------
Emergency Info Hub ([EIH](https://www.e-hub.ie/)),is a fourth year student project, has been designed to be a central website helps the emergency services to prepare for, respond to & recover from disaster, by providing all needed data for the targeted building (E.g. Number of people, area size and emergency exits).
The main objective of this project is giving the number of trapped people under rubbles or inside a building, by tracking their number using a simple movement sensor fitted on the main gate and face detection technology, and save this number to the cloud to be used when a disaster happens.

See [the documentation](http://glasnost.itcarlow.ie/~softeng4/C00220135/index.html#t3) for more detailes.


EIH - Structure:
------------

The structure of the EIH GitHub repository is:

    .
    ├── eih-front-end-webapp/          # The Fron-end folder and files which create the website to output the data.
    ├── eih-raspberrypi-body-detect/   # The Back-end folder and files where all the hardware work takeing place.
    ├── LICENSE                        # EIH LICENSE agreement for any use of the project.            
    └── README.md          


EIH Requirements
------------
This project consist of two parts:

* Hardware: on this link ([Hardware](https://github.com/OAbouHajar/projectEIH/tree/master/eih-raspberrypi-body-detect))
* Website: on this link ([Website](https://github.com/OAbouHajar/projectEIH/tree/master/eih-front-end-webapp))


to run EIH you have to follow the instaction of the REAMDME.MD files for the the Fornt-End and the Back-End.

How EIH works?
------------

<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/documents/back-eng-img/overAll.JPG" alt="mypy logo" width="600px"/>

As It shwon in the diagram above:, 
* EIH breifly works as the following steps:
    * When Some one approach the door, the sesors works and the camera take a picture of the people waking IN Or OUT
    * The Picture will be processed by a body-detect algorithm, to detect how many person in the picture.
    * The total number of people inside the building will be saved on the could (GOOGLE FIREBASE).
    * The Emergency Services will be able to reach this details by the address search at anytime.


What Technologies does EIH use?
------------

<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/documents/back-eng-img/tech.JPG" alt="mypy logo" width="150px"/>


EIH Story
------------

The story of EIH started at that day when this photo was taken (the website background), back to 2012 during the Syrian war,
when I was among those guys running to help the people stuck under rubbles.
during this moments the one and the only question you will hear is: ANYBODY HERE?

The hours, the minutes and even the Seconds might be a reason to give someone a new life. calling again and again... ANYBODY HERE?, feeling bad if any one left behind with no help.

ANYBODY HERE? it's the reason to start, and here where we are: EIH - "EVERY LIFE MATTERS".


EIH Developer
------------
<img src="https://eih.pythonanywhere.com/static/me.png" alt="mypy logo" width="150px"/>

**Osama Abou Hajar** 

**Software Development Engineer**

**Institute of Technology Carlow**

**oabouhajar@hotmail.com**

**Supervisor: Paul Barry**

([EIH](https://www.e-hub.ie/))