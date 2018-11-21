# mike
# 18 November 2018

import piLibe.hygrometer
import piLibe.relay
import piLibe.solenoidValve
import piLibe.suntimes
import time
import RPi.GPIO as GPIO

#=====================================
# initializations
#=====================================

hygrometerChannel = 23
relayChannel = 24
valveChannel = 25

piLibe.hygrometer.initHygrometer( hygrometerChannel )
piLibe.relay.initRelay( relayChannel )
piLibe.solenoidValve.initValve( valveChannel )

rising = piLibe.suntimes.getSunrise() 
shutoff = piLibe.suntimes.getShutOffTime( rising )

#=====================================
# load the hygrometer callback
#=====================================

def tryWater( channel ):
    piLibe.solenoidValve.dispenseWater( valveChannel, hygrometerChannel, 0 )

piLibe.hygrometer.addCallback( hygrometerChannel, tryWater )

#=====================================
# main
#=====================================

while True:
    if( piLibe.suntimes.isSunrise( rising ) ):
        piLibe.relay.enable( relayChannel )
        rising = piLibe.suntimes.getSunrise()
    elif( piLibe.suntimes.isShutOffTime( shutoff ) ):
        piLibe.relay.disable( relayChannel )
        shutoff = piLibe.suntimes.getShutOffTime()
    else:
        pass
    time.sleep(600)

