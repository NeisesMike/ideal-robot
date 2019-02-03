# mike
# 17 November 2018

import RPi.GPIO as GPIO
import time
import utils.logger

GPIO.setmode(GPIO.BCM)

def initButton( channel ):
    GPIO.setup( channel, GPIO.IN, pull_up_down=GPIO.PUD_UP )
    utils.logger.simpleLog( "Button on channel {} initialized".format(channel) )

def isPressed( channel ):
    utils.logger.simpleLog( "Check for button press on channel {}".format(channel) )
    return( not GPIO.input( channel ) )

# don't callback twice in .3 seconds
def addCallback( channel, func ):
    GPIO.add_event_detect( channel, GPIO.BOTH, bouncetime=300 ) # alert when change btwn high/low
    GPIO.add_event_callback( channel, func ) # run callback on change
    utils.logger.simpleLog( "Button callback added" )

