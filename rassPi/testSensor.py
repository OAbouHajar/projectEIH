from gpiozero import MotionSensor
import time
pir = MotionSensor(4)


while True:
    pir.wait_for_motion()
    print("Motion detected")
    pir.wait_for_no_motion()
    print("NO Motion detected")



