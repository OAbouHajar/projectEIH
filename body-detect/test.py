from firebase import firebase
import requests
import pdb
import time
import os
import pyrebase

#export FIREBASE_DB_URL="https://projecteih.firebaseio.com/"
#export DB_FILE_NAME="locations.json"
firebase = firebase.FirebaseApplication('https://projecteih.firebaseio.com', None)
r = requests.get('https://projecteih.firebaseio.com/locations.json')
x= r.json()

def get_all_data_from_firebase():
    r = requests.get('https://projecteih.firebaseio.com/locations.json')
    x= r.json()
    return x
def db_config():
    config = {
    "apiKey": "AIzaSyBa_oAgm7dmE-sFGGm8XG7HYs0gWxVFyJ8",
    "authDomain": "projecteih.firebaseio.com",
    "databaseURL": "https://projecteih.firebaseio.com",
    "storageBucket": "projecteih.appspot.com",
    "serviceAccount": "/home/osama/Desktop/projectEIH/body-detect/cred/projecteih-firebase-adminsdk-dmd9b-dfbc30ba25.json"
    }
    firebasePy = pyrebase.initialize_app(config)

    return firebasePy


def add_new_builiding():
    data_stored = get_all_data_from_firebase()
    data =    {
    'deviceId': 'none',
    'known_name': "AVIVA STADIUM",
    'address' : "AVIVA STADIUM, LANSDOWNE ROAD, DUBLIN 4, IRELAND",
    'eircode' : "R93 V960",
    'numberOfPeopleINDetect': 0,
    'timeUpdated': time.strftime('%X %x %Z'),
    'active' : True
    }
    print(data['address'])
    for key, value in data_stored.items():
        print(key)
        print(value['address'])
        if(str(value['address']) == str(data['address'])):
            return True
    return False

print(add_new_builiding())

