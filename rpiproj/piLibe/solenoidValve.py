# mike
# 17 November 2018

import RPi.GPIO as GPIO
import time
import utils.logger
import hygrometer

GPIO.setmode(GPIO.BCM)

def initValve( channel ):
    GPIO.setup( channel, GPIO.OUT )
    GPIO.output( channel, GPIO.HIGH )
    utils.logger.simpleLog( "Valve on channel {} initialized".format(channel) )

def openFor( channel, aTime ):
    GPIO.output( channel, GPIO.LOW )
    utils.logger.simpleLog( "Valve at {} opened".format(channel) )
    time.sleep( aTime )
    GPIO.output( channel, GPIO.HIGH )
    utils.logger.simpleLog( "Valve at {} closed".format(channel) )

def open( channel ):
    if( GPIO.input(channel) == 0 ):
        return
    GPIO.output( channel, GPIO.LOW )
    utils.logger.simpleLog( "Valve at {} opened".format(channel) )
    
def close( channel ):
    if( GPIO.input(channel) == 1 ):
        return
    GPIO.output( channel, GPIO.HIGH )
    utils.logger.simpleLog( "Valve at {} closed".format(channel) )

