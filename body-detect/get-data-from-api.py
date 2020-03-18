import requests

url = 'https://projecteih.firebaseio.com/carlowIT.json'

r = requests.get(url)
x= r.json()
print(x['numberOfPeopleOut'])