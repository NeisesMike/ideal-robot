# mike
# 18 November 2018

import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )

def initRelay( channel ):
    GPIO.setup( channel, GPIO.OUT )
    GPIO.output( channel, GPIO.HIGH )

def enableFor( channel, aTime ):
    GPIO.output( channel, GPIO.LOW )
    time.sleep( aTime )
    GPIO.output( channel, GPIO.HIGH )

def enable( channel ):
    GPIO.output( channel, GPIO.LOW )
    
def disable( channel ):
    GPIO.output( channel, GPIO.HIGH )

def isEnabled( channel ):
    return( m_enabled )
