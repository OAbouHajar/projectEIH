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
* **configuration** Folder: where configuration files (commonly known simply as config files) are files used to configure the parameters and initial settings for some computer programs, this folder include all [*.cfg and JSON files].
* **static** Folder: Static web pages are often HTML documents stored as files in the file system and made available by the web server over HTTP, this folder include all [*.css, *.png and *.jpg files].
* **templates** Folder: where all the HTML files are stored onherating the base,html page.
* **app.py** File: is the main webapp file where all python code and functions run and work alongside with Flask.
* **.env** File: where all the environment variables are stored and they are represent the security part of the front end.

### .env File ###
- The .env file contain all the environment variables, where all the Tokens, API_Keys, and other type of credentials can be storedas following:

```javascript 
    $ export GOOGLE_API_KEY='GOOGLE-API-KEY-FOR-THE-CREATED-PROJECT-ON-THE-FIREBASE'
    $ export GOOGLE_MAP_API='GOOGLE-MAPS-API-KEY-TO-SHOW-THE-MAP-ON-RESULTS'
    $ export AUTH_DOMAIN='<YOU-PROJECT-NAME-ON-FIREBASE>.firebaseio.com'
    $ export DB_URL='https://<YOU-PROJECT-NAME-ON-FIREBASE>.firebaseio.com'
    $ export STOREG_BUKET='<YOU-PROJECT-NAME-ON-FIREBASE>.appspot.com'
    $ export SERVICE_ACCOUNT='<THE-PATH-TO-THE-DB-CONFIG-JSON-FILE>/projecteih-firebase-adminsdk-dmd9b-dfbc30ba25.json'
    $ export DB_FILE_URL='https://<YOU-PROJECT-NAME-ON-FIREBASE>.firebaseio.com/<THE-JSON-FILE-NAME-ON-FIREBASE>.json'
```


