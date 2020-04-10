<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/img/logo.png" alt="mypy logo" width="150px"/>

EIH: Emergency Info Hub
=======================================

What is EIH?
-------------
Emergency Info Hub ([EIH](https://eih.pythonanywhere.com/)),is a fourth year student project, has been designed to be a central website helps the emergency services to prepare for, respond to & recover from disaster, by providing all needed data for the targeted building (E.g. Number of people, area size and emergency exits).
The main objective of this project is giving the number of trapped people under rubbles or inside a building, by tracking their number using a simple movement sensor fitted on the main gate and face detection technology, and save this number to the cloud to be used when a disaster happens.

See [the documentation](http://glasnost.itcarlow.ie/~softeng4/C00220135/index.html#t3) for more detailes.


EIH - Front-End:
------------
EIH front-end build using ([FLASK](https://flask.palletsprojects.com/en/1.1.x/)) python framework, Jinja2 HTML, CSS, Javascript web design languages. 

The front-end folder include the following directories and files:
* configuration: where configuration files (commonly known simply as config files) are files used to configure the parameters and initial settings for some computer programs, this folder include all [*.cfg and JSON files].
* static: Static web pages are often HTML documents stored as files in the file system and made available by the web server over HTTP, this folder include all [*.css, *.png and *.jpg files].
* templates: where all the HTML files are stored onherating the base,html page.
* app.py file: is the main webapp file where all python code and functions run and work alongside with Flask.