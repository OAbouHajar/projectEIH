import requests

url = 'https://projecteih.firebaseio.com/carlowITUnum.json'

r = requests.get(url)
x= r.json()
print(x['name'])


# while True:
#     r = requests.get(url)
#     x= r.json()
#     status = x['status']
#     while status:
#         print('Project ON')
#         r = requests.get(url)
#         x= r.json()
#         status = x['status']
#     print('Project OFF')


print('exit')