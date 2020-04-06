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
    }
    result = firebase12.post("locations", projectData1)
    print(result)
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
data =    {
            'buildingID': 'it carlow ',
            'deviceId': 'Test ',
            'known_name': 'it carlow ',
            'address' : 'Test Tefffst Test Test Test Test Test Test Test ',
            'eircode' : '1111111111111',
            'numberOfPeopleINDetect': 0,
            'timeUpdated': time.strftime('%X %x %Z')
            }
# Log the user in
db = firebasePy.database()

try:
    user = auth.sign_in_with_email_and_password(email, password)
    #id_API = db.child("locations").child('-M40EmLmh7JjlNpFi2vq').set(data)
    id_API = db.child("locations").push(data)
    print(id_API)
    #patch()
except IOError:
    print ("Oops!  That was no valid number.  Try again...")
