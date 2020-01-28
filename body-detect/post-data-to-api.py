import requests
import time
import datetime
import collections




url = 'https://eihtesting.free.beeceptor.com'
req = requests.get(url)
data = req.json()
print('GET' , data)


urlSend = 'http://eih.mocklab.io/number'
toSendAPI = {
  "numberOfPeopleInside": 2,
  "timeStored": 3
}
reqSend = requests.post(urlSend, params=toSendAPI)
print('POST' , reqSend)
