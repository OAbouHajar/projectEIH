from firebase import firebase
firebase = firebase.FirebaseApplication('https://projecteih.firebaseio.com', None)
import requests


projectData = {    
    "name": "testingFromUnum",
    "buildingID" : "carlowITExit1",
    "deviceId" : "rassPi521",
    "numberOfPeople" : 20,
    "timeUpdated" : "12:21",
    "status" : False,
    }




url = 'https://projecteih.firebaseio.com/carlowITUnum.json'

r = requests.put(url, json=projectData)
x= r.json()
print(x)


#curl -X PUT -d '{"user_id" : "sam", "text" : "Ahoy!"}'   'https://projecteih.firebaseio.com/message_list.json'
