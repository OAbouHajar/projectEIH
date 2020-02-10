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
#camera.resolution = (400,300)

x= True
while x:
    print("project start")
    timeNow = str(datetime.now().strftime("%H,%M,%S"));
    pir.wait_for_motion()
    #camera.capture("/home/pi/year4/projectEIH/rassPi/pictres/"+timeNow+".png")
    camera.capture("/home/pi/year4/projectEIH/body-detect/images/pic.png")
    GPIO.output(18,GPIO.HIGH)
    subprocess.run(["python /home/pi/year4/projectEIH/body-detect/detect.py --images /home/pi/year4/projectEIH/body-detect/images/"], shell=True)
    print("selfie taken  " + timeNow)
    #pir.wait_for_no_motion()
    GPIO.output(18,GPIO.LOW)
    print("LED OFF " + str(datetime.now().strftime("%H,%M,%S")))