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
preNumber = x['numberOfPeopleINDetect']


## read the argument sent from line 55 the detect.py file with the number of new people detected
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--numberOUT", type=int,
help="Current number of people OUT to send to the API")
ap.add_argument("-n2", "--numberIN", type=int,
help="Current number of people IN to send to the API")
args = vars(ap.parse_args())
currentNumberOUT = args["numberOUT"]
currentNumberIN = args["numberIN"]

if args["numberOUT"] is not None:
    ## add the number coming from the API to the number coming from the RassPi
    newNumber = preNumber- currentNumberOUT
elif args["numberIN"] is not None:
    newNumber = preNumber + currentNumberIN


## The Project API
projectData = {
    'buildingID': 'Institute of Technology Carlow',
    'deviceId': 'rassPi4-MainOUT',
    'name': 'Carlow IT MAIN OUT',
    'address' : 'Institute of Technology Carlow, Kilkenny Rd, Moanacurragh, Carlow',
    'eircode' : 'R93 V960',
    'numberOfPeopleINDetect': newNumber,
    'status': True,
    'timeUpdated': time.time()
    }

url = 'https://projecteih.firebaseio.com/carlowIT.json'
## Push the number to the firebase
r = requests.put(url, json=projectData)
x= r.json()
print(x)
print('^^ DONE ^^')