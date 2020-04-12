import RPi.GPIO as GPIO
import time
import picamera
import datetime

sensor1=7
sensor2=18

video = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(sensor2, GPIO.IN, GPIO.PUD_DOWN)

cam=picamera.PiCamera()

### DELAY TIME SHOULE BE 3 SECOND BEFORE THE PIR CHANGE ITS VALUE

def main():
    while True:
        time.sleep(0.5)
        print("DETECTING .....")
        if(GPIO.input(sensor1)):
            print("ONE is ON FIRST")
            time.sleep(2.5)
            if(GPIO.input(sensor2)):
                print("two is ON now")
                print("****************  DONE   *******************")
                time.sleep(3)
                main()
        elif (GPIO.input(sensor2)):
            print("TWO is ON FIRST")
            time.sleep(2.5)
            if(GPIO.input(sensor1)):
                print("IGNORE SENSOR 2 FIRST")
                time.sleep(3)
                main()
main()
