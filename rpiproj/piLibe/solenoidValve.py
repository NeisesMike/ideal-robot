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

def dispenseWater( valveChannel, hygroChannel, attempt ):
    if( attempt > 5 ):
        print( "I must be out of water. Stopping." )
        utils.logger.simpleLog( "VALVE ON CHANNEL {} IS OUT OF WATER".format(valveChannel) )
    elif( hygrometer.isWater(hygroChannel) ):
        print( "Water detected!" )
        time.sleep( 3 )
    else:
        print( "No water detected! Remedying...")
        open( valveChannel )
        attempt += 1
        time.sleep( 5 )
        dispenseWater( valveChannel, hygroChannel, attempt )

