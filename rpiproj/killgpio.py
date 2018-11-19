# mike
# 18 November 2018

import RPi.GPIO as GPIO
import piLibe.relay
import piLibe.hygrometer
import piLibe.solenoidValve

GPIO.setmode( GPIO.BCM )

piLibe.hygrometer.initHygrometer( 23 )
piLibe.relay.initRelay( 24 )
piLibe.solenoidValve.initValve( 25 )

GPIO.cleanup()
