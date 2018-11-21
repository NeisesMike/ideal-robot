# mike
# 18 November 2018

import RPi.GPIO as GPIO
import time
import utils.logger

GPIO.setmode( GPIO.BCM )

def initRelay( channel ):
    GPIO.setup( channel, GPIO.OUT )
    GPIO.output( channel, GPIO.HIGH )
    utils.logger.simpleLog( "Relay on channel {} initialized".format(channel) )

def enableFor( channel, aTime ):
    if( GPIO.input(channel) == 0 ):
        return
    GPIO.output( channel, GPIO.LOW )
    utils.logger.simpleLog( "Relay at {} enabled".format(channel) )
    time.sleep( aTime )
    GPIO.output( channel, GPIO.HIGH )
    utils.logger.simpleLog( "Relay at {} disabled".format(channel) )

def enable( channel ):
    if( GPIO.input(channel) == 0 ):
        return
    GPIO.output( channel, GPIO.LOW )
    utils.logger.simpleLog( "Relay at {} enabled".format(channel) )
    
def disable( channel ):
    if( GPIO.input(channel) == 1 ):
        return
    GPIO.output( channel, GPIO.HIGH )
    utils.logger.simpleLog( "Relay at {} disabled".format(channel) )

def blink( channel ):
    if( GPIO.input(channel) == 1 ):
        enableFor( channel, 1 )
    else:
        disable( channel )
        time.sleep( 1 )
        enable( channel )
    utils.logger.simpleLog( "Relay at {} blinked!".format(channel) )

