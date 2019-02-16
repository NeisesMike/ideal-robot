# mike
# 17 November 2018

import RPi.GPIO as GPIO
import time
import utils.logger

GPIO.setmode(GPIO.BCM)

def initHygrometer( channel ):
    GPIO.setup( channel, GPIO.IN )
    utils.logger.simpleLog( "Hygrometer on channel {} initialized".format(channel) )

def isWater( channel ):
    return( not GPIO.input( channel ) )

## I think if I make bouncetime high, the part will not oxidize so rapidly
def addCallback( channel, func, interval ):
    # must convert interval (minutes) into milliseconds
    milliInterval = interval * 60 * 1000
    # alert when change btwn high/low
    GPIO.add_event_detect( channel, GPIO.BOTH, bouncetime=milliInterval )
    # run callback on change
    GPIO.add_event_callback( channel, func )
    utils.logger.simpleLog( "Hygrometer callback added" )

