import piLibe.relay
import RPi.GPIO as GPIO

piLibe.relay.initRelay( 23 )
piLibe.relay.enableFor( 23, 1 )

GPIO.cleanup()

