import RPi.GPIO as GPIO
import time
import pygame
from datetime import datetime

pygame.mixer.init()

PIR = 7	# On-board pin number 7 (GPIO04)
LED = 12	# On-board pin number 11 (GPIO17)

state = False
val = False
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)	# Change this if using GPIO numbering
GPIO.setup(PIR, GPIO.IN)	# Set PIR as input
GPIO.setup(LED, GPIO.OUT)	# Set LED as output

while True:
    val = GPIO.input(PIR)		# read input value
    if (val == True):		# check if the input is HIGH
        GPIO.output(LED, True)	# turn LED ON
        print("selfie taken  " + str(datetime.now().strftime("%H,%M,%S")))
        if (state == False):
            # ON
            state = True
    else:
        GPIO.output(LED, False)	# turn LED OFF
        print("LED OFF  " + str(datetime.now().strftime("%H,%M,%S")))
        if (state == True):
            # OFF
            time.sleep(2)
            state = False;