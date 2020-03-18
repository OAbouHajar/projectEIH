import time

from gpiozero import MotionSensor
from gpiozero import LED

red_led = LED(17)
red_led.off()

pir = MotionSensor(4)
pir2 = MotionSensor(24)

#start time to check if 2 second pass and no dedect to pir2
startTime = time.time()

def checkWaiting():
    while
    if (time.time() - startTime > 3 ):
        return True





while True:
    if(pir.wait_for_motion()):
        print('Motion detected')
        ## check if no pir2 for 3 second pass and start again
        if(pir2.wait_for_motion()):
            print('2 Motion detected')
            red_led.on()
    pir.wait_for_no_motion()
    print('NO')
    pir2.wait_for_no_motion()
    print('NO 2')
    red_led.off()