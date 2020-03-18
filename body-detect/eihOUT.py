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

#start time to check if 2 second pass and no dedect to pir2
startTime = time.time()

while True:
    if(pir.wait_for_motion()):
        print("pir1 work")
        p = subprocess.run(["python /home/pi/year4/projectEIH/body-detect/subprocessApp2.py"], shell=True)
        pir.wait_for_no_motion()
        print("DONE")