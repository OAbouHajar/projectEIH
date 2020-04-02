from firebase import firebase
import requests
import pdb
import time
import os

#export FIREBASE_DB_URL="https://projecteih.firebaseio.com/"
#export DB_FILE_NAME="locations.json"
firebase = firebase.FirebaseApplication('https://projecteih.firebaseio.com', None)
r = requests.get('https://projecteih.firebaseio.com/locations.json')
x= r.json()

for k, v in x.items():
    print(k)
    print(v['buildingID'])
    print(v['known_name'])
    print(v['eircode'])
    print(v['numberOfPeopleINDetect'])
    print(v['timeUpdated'])
    print('##############################')