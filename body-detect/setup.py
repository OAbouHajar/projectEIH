import argparse
import os
import pdb
import sys

#https://projecteih.firebaseio.com/carlowIT.json
print("################################################################################################")
print("###################################     SETUP START       ######################################")
print("################################################################################################")
## parse the DB URL and set it up as enviroument variable
ap = argparse.ArgumentParser()
ap.add_argument("-db", "--dburl", help="The link to the firebase database",required=True)
ap.add_argument("-r", "--regid", help="the building ID got from the registration", required=True)
ap.add_argument("-dv", "--deviceid", help="the device Id linked to the builiding",required=True)
args = vars(ap.parse_args())
db_url = args["dburl"]
reg_id = args["regid"]
reg_id_fixed = '-'+reg_id
device_id = args["deviceid"]
os.system('export FIREBASE_DB_URL="{}"'.format(db_url))
os.system('export REG_BUILIDING_ID="{}"'.format(reg_id_fixed))
os.system('export DEVICE_ID="{}"'.format(device_id))
#export FIREBASE_DB_URL="https://projecteih.firebaseio.com/locations.json"
#export REG_BUILIDING_ID="-M4AU6aNNx2nxz2qHD2Q"
#export DEVICE_ID="carlow145"
#python3 setup.py --dburl https://projecteih.firebaseio.com/locations.json --regid M4AdyrseXVUYD8UjLEB --deviceid carlow145


print("FIREBASE_DB_URL", os.environ['FIREBASE_DB_URL'])
print("REG_BUILIDING_ID",os.environ['REG_BUILIDING_ID'])
print("DEVICE_ID", os.environ['DEVICE_ID'])

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
os.system('pip3 install Crypto')
os.system('pip install pyrebase')
os.system('pip3 install pyrebase')

print("################################################################################################")
print("###################################     SETUP DONE        ######################################")
print("################################################################################################")