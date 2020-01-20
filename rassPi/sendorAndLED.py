from gpiozero import MotionSensor
from picamera import PiCamera
import time
import RPi.GPIO as GPIO
from datetime import datetime


x= True
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


pir = MotionSensor(4)
camera = PiCamera()
camera.rotation = 180


while True:
    timeNow = str(datetime.now().strftime("%H,%M,%S"));
    pir.wait_for_motion()
    camera.capture("/home/pi/year4/emergencyIH/rassPi/pictres/"+timeNow+".png")
    GPIO.output(18,GPIO.HIGH)
    print("selfie taken  " + timeNow)
    pir.wait_for_no_motion()
    GPIO.output(18,GPIO.LOW)
    print("LED OFF " + str(datetime.now().strftime("%H,%M,%S")))