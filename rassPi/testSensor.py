from gpiozero import MotionSensor
from picamera import PiCamera
import time
import RPi.GPIO as GPIO

x= True
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

pir = MotionSensor(4)
camera = PiCamera()

while x:
    pir.wait_for_motion()
    camera.capture("/home/pi/selfie.png")
    GPIO.output(18,GPIO.HIGH)
    print("selfie taken")
    pir.wait_for_motion()
    GPIO.output(18,GPIO.HIGH)
    print("selfie taken")


camera.close()
GPIO.output(18,GPIO.LOW)