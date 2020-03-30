import RPi.GPIO as GPIO
from threading import Thread

## sensors connection
BEAM_PIN1 = 18 ##sensor Number !
BEAM_PIN2 = 17 ##sensor Number 2

def ir1First(channel):
    print('one First')
    print('WAIT TWO >>>>')
    channel = GPIO.wait_for_edge(BEAM_PIN2, GPIO.RISING, timeout=1000)
    if channel is None:
        print('Timeout occurred')
    else:
        print('CAMERA', channel)
        pass

## set the pins mode
GPIO.setmode(GPIO.BCM)
## set up the sensors to the rass pi
GPIO.setup(BEAM_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BEAM_PIN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
## If any beam break happened for the sensor 1 callback the funstion to check sensor 2
GPIO.add_event_detect(BEAM_PIN1, GPIO.RISING, callback=ir1First, bouncetime=200)


#exit the program when user press enter.
message = input("Press enter to quit\n\n")
GPIO.cleanup()