import piLibe.relay
import RPi.GPIO as GPIO
import time

piLibe.relay.initRelay( 24 )
piLibe.relay.enableFor( 24, 1 )

GPIO.cleanup()

