# mike
# 18 November 2018

import piLibe.suntimes
import piLibe.hygrometer
import piLibe.relay
import piLibe.solenoidValve
import time
import RPi.GPIO as GPIO

#=====================================
# initialize the components
#=====================================

hygrometerChannel = 23
relayChannel = 24
valveChannel = 25

piLibe.hygrometer.initHygrometer( hygrometerChannel )
piLibe.relay.initRelay( relayChannel )
piLibe.solenoidValve.initValve( valveChannel )

#=====================================
# load the hygrometer callback
#=====================================

def tryWater( channel ):
    piLibe.solenoidValve.dispenseWater( valveChannel, hygrometerChannel, 0 )

piLibe.hygrometer.addCallback( hygrometerChannel, tryWater )

#=====================================
# calculate sun times
#=====================================

rising = piLibe.suntimes.getSunrise() 
setting = piLibe.suntimes.getSunset()

#=====================================
# main
#=====================================

while True:
    if( piLibe.suntimes.isSunrise( rising ) ):
        piLibe.relay.enable( relayChannel )
        rising = piLibe.suntimes.getSunrise()
    elif( piLibe.suntimes.isSunset( setting ) ):
        piLibe.relay.disable( relayChannel )
        setting = piLibe.suntimes.getSunrise()
    else:
        pass
    time.sleep(5)

GPIO.cleanup()
