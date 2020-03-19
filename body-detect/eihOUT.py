import time
from gpiozero import MotionSensor
from gpiozero import LED
import subprocess
import os
import signal

red_led = LED(17)
red_led.off()

pir = MotionSensor(4)
pir2 = MotionSensor(24)

## run the project for ever.
while True:
    print('PIR ONE DETECTING ....')
    if(pir.wait_for_motion()):
        print("> PIR ONE ON < ")
        ## once the First sensor is ON
        ## another process will run to check sensor two
        p = subprocess.run(["python /home/pi/year4/projectEIH/body-detect/subprocessApp2.py"], shell=True)
        ##### HERE I NEED THE HELP: NOW THE PROCESS RUN IN THE BACKGROUBD AND ANOTHER PROCESS READY TO GO
        ##### LIKE: p2 = ... IS WAITING WHILE p .. IS WORKING
        pir.wait_for_no_motion()
        print("STORED")