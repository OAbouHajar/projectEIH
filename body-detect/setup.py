import argparse
import os
import pdb
import sys

#https://projecteih.firebaseio.com/carlowIT.json
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