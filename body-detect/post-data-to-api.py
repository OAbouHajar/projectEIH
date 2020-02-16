from firebase import firebase
firebase = firebase.FirebaseApplication('https://projecteih.firebaseio.com', None)
import requests



projectData = {
    'buildingID': 'carlowITExit1',
    'deviceId': 'rassPi521',
    'name': 'Carlow IT Unum',
    'numberOfPeopleIn': 1,
    'numberOfPeopleOut': 0,
    'status': False,
    'timeUpdated': '12:21'}

url = 'https://projecteih.firebaseio.com/carlowIT.json'

r = requests.put(url, json=projectData)
x= r.json()
print(x)


#curl -X PUT -d '{"user_id" : "sam", "text" : "Ahoy!"}'   'https://projecteih.firebaseio.com/message_list.json'
