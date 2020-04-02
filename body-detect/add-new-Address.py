from firebase import firebase
import requests
import pdb
import time
import os

#export FIREBASE_DB_URL="https://projecteih.firebaseio.com/"
#export DB_FILE_NAME="locations.json"

def patch():
    firebase12 = firebase.FirebaseApplication('https://projecteih.firebaseio.com', None)
    ## get the previouse number on the API
    url = 'https://projecteih.firebaseio.com/'

    projectData1 = {
            'Test Test Test':
            {
            'buildingID': 'Test ',
            'deviceId': 'Test ',
            'known_name': 'Test ',
            'address' : 'Test Tefffst Test Test Test Test Test Test Test ',
            'eircode' : 'sdasdasdasd ',
            'numberOfPeopleINDetect': 0,
            'timeUpdated': time.strftime('%X %x %Z')
            },
            'Carlow IT MAIN Entrance':
        {
        'buildingID': 'Institute of Technology Carlow',
        'deviceId': 'rassPi4-MainOUT',
        'known_name': 'Carlow IT MAIN Entrance',
        'address' : 'Institute of Technology Carlow, Kilkenny Rd, Moanacurragh, Carlow',
        'eircode' : 'R93 V960',
        'numberOfPeopleINDetect': 0,
        'timeUpdated': time.strftime('%X %x %Z')
        }, 
        'portlaoise garda station':
        {
        'buildingID': 'AN GARDA SIOCHANA',
        'deviceId': 'rassPi4-MainOUT',
        'known_name': 'portlaoise garda station',
        'address' : 'PORTLAOISE GARDA STATION ABBEYLEIX ROAD PORTLAOISE CO. LAOIS',
        'eircode' : 'R32 XW68',
        'numberOfPeopleINDetect': 0,
        'timeUpdated': time.strftime('%X %x %Z')
        }
    }
    result = firebase12.patch("locations", projectData1)
    return result



import pyrebase

config = {
"apiKey": "AIzaSyBa_oAgm7dmE-sFGGm8XG7HYs0gWxVFyJ8",
"authDomain": "projecteih.firebaseio.com",
"databaseURL": "https://projecteih.firebaseio.com",
"storageBucket": "projecteih.appspot.com",
"serviceAccount": "/home/osama/Desktop/projectEIH/body-detect/cred/projecteih-firebase-adminsdk-dmd9b-dfbc30ba25.json"
}


firebasePy = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebasePy.auth()

email = 'oabouhajar@hotmail.com'
password = '1qaz2wsx@'

# Log the user in
try:
    user = auth.sign_in_with_email_and_password(email, password)
    patch()
except IOError:
    print ("Oops!  That was no valid number.  Try again...")
