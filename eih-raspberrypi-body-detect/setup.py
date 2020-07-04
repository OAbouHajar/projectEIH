import argparse
import os
import pdb
import sys

#export FIREBASE_DB_URL=https://projecteih.firebaseio.com/locations.json
#export REG_BUILIDING_ID=-M4Eq45nYdyBOA8GgL5r
#export DEVICE_ID=carlow14512
#export PROJECT_API_KEY=<>
#os.environ['PROJECT_API_KEY']
print("################################################################################################")
print("###################################     SETUP START       ######################################")
print("################################################################################################")
##installing python

os.system('sudo apt-get update')
os.system('sudo apt-get install python3.6')
## Installing pip
os.system('curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"')
os.system('python get-pip.py')
os.system('python3 get-pip.py')      # For specific python version
## Install all python dependency
os.system('sudo apt update && sudo apt-get install python-opencv python-scipy ipython')
os.system('pip install opencv-python')
os.system('sudo pip install requests')
os.system('sudo pip install python-firebase')
os.system('pip3 install firebase')
os.system('pip install imutils')
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
