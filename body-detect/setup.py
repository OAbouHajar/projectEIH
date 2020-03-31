import argparse
import os
import pdb
import sys

#https://projecteih.firebaseio.com/carlowIT.json

## parse the DB URL and set it up as enviroument variable
ap = argparse.ArgumentParser()
ap.add_argument("-db", "--dburl", help="The link to the firebase database")
args = vars(ap.parse_args())
db_url = args["dburl"]
os.system('export FIREBASE_DB_URL="{}"'.format(db_url))
##installing python 
os.system('sudo apt-get update')
os.system('sudo apt-get install python3.6')
## Installing pip
os.system('curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"')
os.system('python get-pip.py')     
os.system('python3 get-pip.py')      # For specific python version 
## Install all python dependency 
os.system('sudo pip install requests')
os.system('sudo pip install python-firebase')
os.system('pip3 install firebase')
os.system('pip3 install imutils')
os.system('pip3 install python_jwt')
os.system('pip3 install gcloud')
os.system('pip3 install sseclient')
os.system('pip3 install parse')
os.system('pip3 install requests_toolbelt')
os.system('pip3 install flask')

