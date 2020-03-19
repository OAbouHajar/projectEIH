import time
from gpiozero import MotionSensor
from gpiozero import LED
import subprocess
import os
from picamera import PiCamera
import RPi.GPIO as GPIO
from datetime import datetime
## LED Temporory TO BE DELETED AFTER
red_led = LED(17)
red_led.off()
## PIR Sensors Conections
pir = MotionSensor(4)
pir2 = MotionSensor(24)
## Camera Configuration
camera = PiCamera()
camera.resolution = (400,200)

## HERE: THE SUBPROCESS (P) IS RUNNING IS THAT CORRECT ?
print('PIR TWO WAITING ....')
pir2.wait_for_motion()
print('> PIR TWO ON <')
print ('*** PICTURE TAKEN ***')
camera.capture("/home/pi/year4/projectEIH/body-detect/images/pic.png")
print ('++++ BODY DETECTING ++++ ')
## IS IT THE SAME SUBPROCESS ?
subprocess.call(["python /home/pi/year4/projectEIH/body-detect/detect.py --images /home/pi/year4/projectEIH/body-detect/images/"], shell=True)
red_led.on()
pir2.wait_for_no_motion()
exit()