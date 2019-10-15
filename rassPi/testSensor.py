from gpiozero import MotionSensor
from picamera import PiCamera
import time


pir = MotionSensor(4)
camera = PiCamera()

while True:
    if(pir.wait_for_motion()):
        camera.capture("/home/pi/selfie.png")
        print("selfie taken")


camera.close()