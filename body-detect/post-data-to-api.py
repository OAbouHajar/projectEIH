from firebase import firebase
import requests
import argparse
import time

## connection to the firebase
firebase = firebase.FirebaseApplication('https://projecteih.firebaseio.com', None)

## get the previouse number on the API
url = 'https://projecteih.firebaseio.com/carlowIT.json'
r = requests.get(url)
x= r.json()
preNumber = x['numberOfPeopleOut']


## read the argument sent from line 55 the detect.py file with the number of new people detected
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--numberOUT", type=int,
help="Current number of people to send to the API")
args = vars(ap.parse_args())
currentNumber = args["numberOUT"]

## add the number coming from the API to the number coming from the RassPi
newNumber = preNumber + currentNumber

## The Project API
projectData = {
    'buildingID': 'CarlowIT',
    'deviceId': 'rassPi4-MainOUT',
    'name': 'Carlow IT MAIN OUT',
    'numberOfPeopleIn': 0,
    'numberOfPeopleOut': newNumber,
    'status': False,
    'timeUpdated': time.time()}

url = 'https://projecteih.firebaseio.com/carlowIT.json'
## Push the number to the firebase
r = requests.put(url, json=projectData)
x= r.json()
print(x)