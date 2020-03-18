import time

from gpiozero import MotionSensor
from gpiozero import LED

pir = MotionSensor(4)
red_led = LED(17)
red_led.off()

pir2 = MotionSensor(24)

while True:
    pir.wait_for_motion()
    print('Motion detected')
    pir2.wait_for_motion()
    print('2 Motion detected')
    red_led.on()
    pir.wait_for_no_motion()
    print('NO')
    pir2.wait_for_no_motion()
    print('NO 2')
    red_led.off()