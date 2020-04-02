from firebase import firebase
import requests

## connection to the firebase
firebase = firebase.FirebaseApplication('https://projecteih.firebaseio.com', None)
## get the previouse number on the API
url = 'https://projecteih.firebaseio.com/carlowIT.json'
r = requests.get(url)
x= r.json()


uid = 'some-uid'

custom_token = auth.create_custom_token(uid)