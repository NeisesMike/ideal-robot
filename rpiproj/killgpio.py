# mike
# 20 november 18

import piLibe.hygrometer
import piLibe.relay
import piLibe.solenoidValve
import RPi.GPIO as GPIO

gpios = [23,24,25,16,17,27,22,26]

def initInput( channel ):
    GPIO.setup( channel, GPIO,IN )

def initOutput( channel ):
    GPIO.setup( channel, GPIO.OUT )


for i in gpios:
    try:
        initInput( i )
    except:
        pass
    try:
        initOutput( i )
    except:
        pass

GPIO.cleanup()
