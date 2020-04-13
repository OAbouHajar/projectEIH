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

The structure of the front-en is:

    .
    ├── configuration       # Configure the parameters and initial settings for some computer programs               
    ├── static              # Static web pages are HTML documents stored as files in the file system and made available by the web server over HTTP
    ├── templates           # All the HTML files are stored onherating the base,html page
    ├── app.py              # The main webapp python file where all python code and functions run and work alongside with Flask. 
    ├── .env                # All the environment variables are stored and they are represent the security part of the front end.
    ├── requirements.txt    # EIH enviroument requirements.            
    └── README.md           #

### app.py ###
-- This is the main file for the webApp, all the function and the variables are getting processed,to run the file you need to have the following dependencies installed on you machine, or on the server side for online deployment.

To run the app you need to have Python3 installed and flask, in addition to the ([request](https://pypi.org/project/requests/)), ([firebase](https://pypi.org/project/firebase/)), ([python-dotenv](https://pypi.org/project/python-dotenv/)), ([pyrebase](https://pypi.org/project/python-dotenv/)) dependencies as the following:

```javascript
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python get-pip.py
python3 get-pip.py
pip3 install flask
pip install requests
pip install python-firebase
pip3 install firebase
pip install python-dotenv
pip3 install pyrebase
```
This dependencies will be responsable on all the process and the connections between the DataBase and the WebApp.

### .env File ###
-- The .env file contain all the environment variables, where all the Tokens, API_Keys, and other type of credentials can be storedas following:

```javascript 
    $ export GOOGLE_API_KEY='GOOGLE-API-KEY-FOR-THE-CREATED-PROJECT-ON-THE-FIREBASE'
    $ export GOOGLE_MAP_API='GOOGLE-MAPS-API-KEY-TO-SHOW-THE-MAP-ON-RESULTS'
    $ export AUTH_DOMAIN='<YOU-PROJECT-NAME-ON-FIREBASE>.firebaseio.com'
    $ export DB_URL='https://<YOU-PROJECT-NAME-ON-FIREBASE>.firebaseio.com'
    $ export STOREG_BUKET='<YOU-PROJECT-NAME-ON-FIREBASE>.appspot.com'
    $ export SERVICE_ACCOUNT='<THE-PATH-TO-THE-DB-CONFIG-JSON-FILE>/projecteih-firebase-adminsdk-dmd9b-dfbc30ba25.json'
    $ export DB_FILE_URL='https://<YOU-PROJECT-NAME-ON-FIREBASE>.firebaseio.com/<THE-JSON-FILE-NAME-ON-FIREBASE>.json'
```

> For more detailes about Google firebase and Google Address autocomplete and how to get this API_KEYS and Tokens, You have to register and read Google docomentations 
* ([Goolge Firebase](https://firebase.google.com/))
* ([Goolge Maps API](https://cloud.google.com/maps-platform/))

EIH - Screens & Code Functionality:
------------

### Search Screen: ### 
It is the main screen of the project, it contain a number of componentes and functions to run. 

<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/documents/front-end-img/main.JPG" alt="mypy logo" width="600px"/>


1. **The Search input:**
   The search box has an integrated Address autocomplete, which create a compatibility to have one search mechanizm.
   In this screen the user can seach for any Irish addresses 
   The search box use the Google Auto complete API to give the user the ability to get the correct address and save their time during emergency moments.
   To be able to list the address from another countries than Ireland, the country code with in the restrictions atribute in the files below should 

* `templates/googlAutoCompleteGeneral.html`
* `templates/googlAutoComplete.html`

```javascript
        // Change the country code from 'IE' to the country where is EIH used 
        // to be able to list al locations with in this country 
        autocomplete.setComponentRestrictions({
            'country': 'IE'
        });
```

  For more informations about the ([Google Addresses Autocomplete](https://developers.google.com/maps/documentation/javascript/places-autocomplete?utm_source=google&utm_medium=cpc&utm_campaign=FY18-Q2-global-demandgen-paidsearchonnetworkhouseads-cs-maps_contactsal_saf&utm_content=text-ad-none-none-DEV_c-CRE_397052992739-ADGP_Hybrid+%7C+AW+SEM+%7C+SKWS+~+Places+%7C+BMM+%7C+Address+Autocomplete-KWID_43700049595992256-kwd-312924430504-userloc_20479&utm_term=KW_%2Baddress%20%2Bautocomplete-ST_%2Baddress+%2Bautocomplete&gclid=CjwKCAjw1cX0BRBmEiwAy9tKHirhZ_N53PbWLuOTp3QmQuashEdWHHrzFS0_AOuHn5pBLkcqdNTJjBoC-8kQAvD_BwE)) and the ([countries code](https://www.iban.com/country-codes)).


2. **The Search Button:**
The search button will send a `POST` request to the `app.py` file to run the `display_form():` function.
This function will be calling another functions to get the data and check from the database and check if the address is already registerd and active or not.

* if the fucntions returns `True` the `retult.html` bage will be display with all the data coming from the Database, in addition to Google Map box using the `maps2.html` file.
<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/documents/front-end-img/results%20screen.JPG" alt="mypy logo" width="600px"/>

* if the fucntions returns `False` the app will be redirected to the main page with allert no data for the searched address founded displayed.
<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/documents/front-end-img/alert_not_founded.JPG" alt="mypy logo" width="600px"/>


### Loactions Screen: ### 
This screen will display all the locations with in the databases, and give a fully dymaic table to the admins to add, delete, update, and reset the number of people for each row.

* Public access all locations page:

<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/documents/front-end-img/all_locations.JPG" alt="mypy logo" width="600px"/>

* Admis access all locations page with the menu options on the right mouse click:

<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/documents/front-end-img/all_locations_admin.JPG" alt="mypy logo" width="600px"/>

#### Add Building Feature ####
> This is the one of the most important parts to link the hardware to the database:

To add building you have to login as Admin (If you have no Access you sould contact the admin body create a credential for to gain an access).
Then you follow the steps in the picture:

<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/documents/front-end-img/add_building_steps.JPG" alt="mypy logo" width="600px"/>

* Once you have registration completed the System will show you the Building registration ID, This ID should be used on the hardware side to link the backend to this actual building, as it show in the picture.

<img src="http://glasnost.itcarlow.ie/~softeng4/C00220135/documents/front-end-img/alert_added_new_key.JPG" alt="mypy logo" width="600px"/>

* if the Alert! Massege was telling the building is already in the system, that means the building should be activated again and the buidling ID is already assigned.

#### Update Building Feature ####
On the All locations page, the table support the edit mode, double click on the row you want to edit and you have the ability to edit one row at the time, then you sleeted the radio bottom for the edited row and select the update option from the menu.

#### Reset Building Feature ####
To Reset a building, select the building row, and select the reset option from the table menu. The number of people inside the selected building will be reset to zero.

#### Delete Building Feature ####
The Delete option from table menu, will update the  `active` value in the database to `False`.

```python 
{"active": False}
```

#### Activate Building Feature ####
The Activate option from table menu, will updagte the `active` value in the database to `True`.

```python 
{"active": True}
```

#### About Us Screen ####

The project description and the story of the project.

#### Case Study Screen ####

Redirect to an external link to show the show the case study for EIH as a final year project.

#### Contact Screen ####

A contact form to allow the users to contact the admins to give feedback or to report an problem.

EIH - API and Database Structure:
------------
EIH data stored as an API on Google firebase real time database.
The data are formatted  as JSON with dictionary key and value.


```python
data =
{
   '<BUILDING-ID>': {                                                           # AUTO GENERATED WITH PUSH REQUEST WHEN THE DATA GET ADDED.
        'active' : '<BOOLEAN-VALUE>',                                           # True for active and False for not active.
        "deviceId": '<STRING-SET-BY-THE-USERS-FROM-THE-BACK-END>',              # To be choosen by the developer at the instalment time
        "known_name": '<THE-BUILDING-KNOWN-NAME>',                              # The known building name
        "address": '<THE-ADDRESS-GENERATED-BY-GOOGLE-ADDRESS-AUTOCOMPLETE>',    # Should be uniqe and this is the main link poin to the item
        "eircode": '<THE-BUILDING-EIRCODE>',                                    # NOT USER IN FOR ALL IRSH ADDRESSES.
        "numberOfPeopleINDetect": '<INTEGER-INITIALIZED-TO-ZERO>',              # Integer value - initialized to zero.
        "timeUpdated": '<AUTO-GENERATED-BY-THE-SERVER-TIME>'                   # DateTime Value - Generated by the server 
    }
}
```


> For more details you can refare to the comment with in each file, or contact the developer by email. 