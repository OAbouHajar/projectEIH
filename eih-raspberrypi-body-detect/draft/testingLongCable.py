import RPi.GPIO as GPIO
from threading import Thread


BEAM_PIN2 = 17
BEAM_PIN1 = 18

def ir1First(channel):
    print('one First')
    print('WAIT TWO >>>>')
    channel = GPIO.wait_for_edge(BEAM_PIN2, GPIO.RISING, timeout=1000)
    if channel is None:
        print('Timeout occurred')
    else:
        print('CAMERA', channel)
        pass


GPIO.setmode(GPIO.BCM)
GPIO.setup(BEAM_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BEAM_PIN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(BEAM_PIN1, GPIO.RISING, callback=ir1First, bouncetime=200)



message = input("Press enter to quit\n\n")
GPIO.cleanup()