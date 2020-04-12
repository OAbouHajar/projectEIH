from firebase import firebase
import requests
import pdb
import time
## connection to the firebase
firebase = firebase.FirebaseApplication('https://projecteih.firebaseio.com', authentication=None)
## get the previouse number on the API
url = 'https://projecteih.firebaseio.com/'

projectData = {
        'Carlow IT MAIN Entrance':
        {
        'buildingID': 'Institute of Technology Carlow',
        'deviceId': 'rassPi4-MainOUT',
        'known_name': 'Carlow IT MAIN Entrance',
        'address' : 'Institute of Technology Carlow, Kilkenny Rd, Moanacurragh, Carlow',
        'eircode' : 'R93 V960',
        'numberOfPeopleINDetect': 0,
        'timeUpdated': time.time()
        }, 
        'portlaoise garda station':
        {
        'buildingID': 'AN GARDA SIOCHANA',
        'deviceId': 'rassPi4-MainOUT',
        'known_name': 'portlaoise garda station',
        'address' : 'PORTLAOISE GARDA STATION ABBEYLEIX ROAD PORTLAOISE CO. LAOIS',
        'eircode' : 'R32 XW68',
        'numberOfPeopleINDetect': 0,
        'timeUpdated': time.time()
        }
}

projectData1 = {
        'Test Test Test':
        {
        'buildingID': 'Test ',
        'deviceId': 'Test ',
        'known_name': 'Test ',
        'address' : 'Test Tefffst Test Test Test Test Test Test Test ',
        'eircode' : 'sdasdasdasd ',
        'numberOfPeopleINDetect': 0,
        'timeUpdated': time.time()
        }
}



# data = {'url': url, 
#         'address': 'addr11111111ess',
#         'name': 'name',
#         'auth':'AIzaSyBa_oAgm7dmE-sFGGm8XG7HYs0gWxVFyJ8'
#         }

result = firebase.patch("locations", projectData1)

