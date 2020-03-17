# Write your code here :-)
from gpiozero import MotionSensor
from picamera import PiCamera
import RPi.GPIO as GPIO
from datetime import datetime
import subprocess

pir = MotionSensor(4)


x= True
while x:
    print("project start")
    pir.wait_for_motion()
    print("selfie taken  ")