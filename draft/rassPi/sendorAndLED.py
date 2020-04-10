from gpiozero import MotionSensor
from picamera import PiCamera
import time
import RPi.GPIO as GPIO
from datetime import datetime
import subprocess

x= True
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


pir = MotionSensor(4)
camera = PiCamera()
camera.rotation = 180
camera.resolution = (400,300)

x= True
while x:
    timeNow = str(datetime.now().strftime("%H,%M,%S"));
    pir.wait_for_motion()
    #camera.capture("/home/pi/year4/projectEIH/rassPi/pictres/"+timeNow+".png")
    camera.capture("/home/pi/year4/projectEIH/rassPi/pictres/pic.png")
    GPIO.output(18,GPIO.HIGH)
    subprocess.run(["python ~/year4/projectEIH/rassPi/face_detect.py ~/year4/projectEIH/rassPi/pictres/pic.png ~/year4/projectEIH/rassPi/haarcascade_frontalface_default.xml"], shell=True)
    print("selfie taken  " + timeNow)
    pir.wait_for_no_motion()
    GPIO.output(18,GPIO.LOW)
    print("LED OFF " + str(datetime.now().strftime("%H,%M,%S")))
    x = False
