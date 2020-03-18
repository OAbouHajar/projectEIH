from firebase import firebase
firebase = firebase.FirebaseApplication('https://projecteih.firebaseio.com', None)
import requests
import argparse
import time

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--numberOUT", type=int,
help="Current number of people to send to the API")

args = vars(ap.parse_args())

currentNumber = args["numberOUT"]
print ('currentNumber' , currentNumber)
projectData = {
    'buildingID': 'CarlowIT',
    'deviceId': 'rassPi4-MainOUT',
    'name': 'Carlow IT MAIN OUT',
    'numberOfPeopleIn': 0,
    'numberOfPeopleOut': currentNumber,
    'status': False,
    'timeUpdated': time.time()}

url = 'https://projecteih.firebaseio.com/carlowIT.json'

r = requests.put(url, json=projectData)
x= r.json()
print(x)


#curl -X PUT -d '{"user_id" : "sam", "text" : "Ahoy!"}'   'https://projecteih.firebaseio.com/message_list.json'