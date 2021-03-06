import RPi.GPIO as GPIO
import subprocess
import argparse
import os
import pdb
import sys
from picamera import PiCamera
from datetime import datetime
import time

## Camera Configuration
camera = PiCamera()
camera.resolution = (400,200)


## Sensors Configuration
BEAM_PIN1 = 4  ##sensor Number !
BEAM_PIN2 = 17 ##sensor Number 2


##current working directory
path = os.getcwd()
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
listArg =  sys.argv[1:]
direction = listArg[0]


def ir1First(channel):
    print('one First')
    print('WAIT TWO >>>>')
    ## ignoring further edges for 1000ms and wait for one again
    channel = GPIO.wait_for_edge(BEAM_PIN2, GPIO.RISING, timeout=1000)
    ## when the sensor 2 beam break then we start the process
    if channel is None:
        print('Timeout occurred')
    else:
        ## if sensor two was detected the camera run to take picture
        print('CAMERA', channel)
        print ('*** PICTURE TAKEN ***')
        camera.capture("{}/images/pic.png".format(path))
        #timeNow = str(datetime.now().strftime("%H,%M,%S"));
        #camera.capture("/home/pi/year4/projectEIH/body-detect/images/pic"+timeNow+".png")
        print ('++++ BODY DETECTING ++++ ')
        command = "python {}/detect.py --images {}/images/ -d {}".format(path,path, direction )
        subprocess.call([command], shell=True)




## set the pins mode
GPIO.setmode(GPIO.BCM)
## set up the sensors to the rass pi
GPIO.setup(BEAM_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BEAM_PIN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
## If any beam break happened for the sensor 1 callback the funstion to check sensor 2
# ignoring further edges for 200ms for switch bounce handling
GPIO.add_event_detect(BEAM_PIN1, GPIO.RISING, callback=ir1First, bouncetime=200)

#exit the program when user press enter.
message = input("Press enter to quit\n\n")
GPIO.cleanup()