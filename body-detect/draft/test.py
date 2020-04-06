from firebase import firebase
import requests
import argparse
import time
import os
import pyrebase



def get_stored_number_of_people_from_db(reg_id):
    r = requests.get('https://projecteih.firebaseio.com/locations.json')
    x= r.json()
    return x[reg_id]['numberOfPeopleINDetect']


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


def update_with_the_new_number(id_to_reset, new_number):
    db = db_config().database()
    x= db.child("locations").child(id_to_reset).update({'numberOfPeopleINDetect': new_number})
    return x

print(get_stored_number_of_people_from_db('-M4AU6aNNx2nxz2qHD2Q'))
print(update_with_the_new_number('-M4AU6aNNx2nxz2qHD2Q',10))