# mike
# 17 November 2018

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def initValve( channel ):
    GPIO.setup( channel, GPIO.OUT )
    GPIO.output( channel, GPIO.HIGH )

def openFor( channel, aTime ):
    GPIO.output( channel, GPIO.LOW )
    time.sleep( aTime )
    GPIO.output( channel, GPIO.HIGH )

def open( channel ):
    GPIO.output( channel, GPIO.LOW )
    
def close( channel ):
    GPIO.output( channel, GPIO.HIGH )

def dispenseWater( valveChannel, hygroChannel, attempt ):
    if( attempt > 5 ):
        print( "I must be out of water. Stopping." )
    elif( GPIO.input( hygroChannel ) ):
        print( "No water detected! Remedying...")
        open( valveChannel )
        attempt += 1
        time.sleep( 5 )
        dispenseWater( valveChannel, hygroChannel, attempt )
    else:
        print( "Water detected!" )
        time.sleep( 3 )

