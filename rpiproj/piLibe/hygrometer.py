# mike
# 17 November 2018

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def initHygrometer( channel ):
    GPIO.setup( channel, GPIO.IN )

def isWater( channel ):
    return( not GPIO.input( channel ) )

# don't callback twice in five seconds
def addCallback( channel, func ):
    GPIO.add_event_detect( channel, GPIO.BOTH, bouncetime=5000 ) # alert when change btwn high/low
    GPIO.add_event_callback( channel, func ) # run callback on change

