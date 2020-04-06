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

## get the previouse number on the API
url = os.environ['FIREBASE_DB_URL']
reg_id = os.environ['REG_BUILIDING_ID']
device_id = os.environ['DEVICE_ID']


## read the argument sent from line 55 the detect.py file with the number of new people detected
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--numberOUT", type=int,
help="Current number of people OUT to send to the API")
ap.add_argument("-n2", "--numberIN", type=int,
help="Current number of people IN to send to the API")
args = vars(ap.parse_args())
currentNumberOUT = args["numberOUT"]
currentNumberIN = args["numberIN"]

## get the previous number from the DB
preNumber = get_stored_number_of_people_from_db(reg_id)

if args["numberOUT"] is not None:
    ## substact the number coming from the API to the number coming from the RassPi
    newNumber = preNumber- currentNumberOUT
elif args["numberIN"] is not None:
    ## add the number coming from the API to the number coming from the RassPi
    newNumber = preNumber + currentNumberIN

## send the new number to the update with the building ID
update_with_the_new_number(reg_id, newNumber)