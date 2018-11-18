# mike
# 17 November 2018

import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )
GPIO.setup( 24, GPIO.OUT )
GPIO.output( 24, GPIO.HIGH )

def goMotor( aTime ):
    GPIO.output( 24, GPIO.LOW )
    time.sleep( aTime )
    GPIO.output( 24, GPIO.HIGH )

goMotor( 1 )
time.sleep( 1 )

GPIO.cleanup()










