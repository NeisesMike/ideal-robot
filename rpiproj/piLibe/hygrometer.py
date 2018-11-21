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

# don't callback twice in .3 seconds
def addCallback( channel, func ):
    GPIO.add_event_detect( channel, GPIO.BOTH, bouncetime=300 ) # alert when change btwn high/low
    GPIO.add_event_callback( channel, func ) # run callback on change
    utils.logger.simpleLog( "Hygrometer callback added" )

