from firebase import firebase
firebase = firebase.FirebaseApplication('https://projecteih.firebaseio.com', authentication=None)
result = firebase.get('/users', None, {'print': 'pretty'})
print (result)
