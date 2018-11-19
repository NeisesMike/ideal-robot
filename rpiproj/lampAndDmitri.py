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

valveChannel = 22
hygrometerChannel = 23
plantRelayChannel = 24
dmitriRelayChannel = 25

piLibe.solenoidValve.initValve( valveChannel )
piLibe.hygrometer.initHygrometer( hygrometerChannel )
piLibe.relay.initRelay( plantRelayChannel )
piLibe.relay.initRelay( dmitriRelayChannel )

rising = piLibe.suntimes.getSunrise() 
setting = piLibe.suntimes.getSunset()
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

# boot-time tests
piLibe.relay.enableFor( plantRelayChannel, 1 )
piLibe.relay.enableFor( dmitriRelayChannel, 1 )

while True:
    if( piLibe.suntimes.isSunrise( rising ) ):
        piLibe.relay.enable( plantRelayChannel )
        piLibe.relay.enable( dmitriRelayChannel )
        rising = piLibe.suntimes.getSunrise()

    elif( piLibe.suntimes.isSunset( setting) ):
        piLibe.relay.disble( dmitriRelayChannel )
        setting = piLibe.suntimes.getSunset()

    elif( piLibe.suntimes.isShutOffTime( shutoff ) ):
        piLibe.relay.disable( plantRelayChannel )
        shutoff = piLibe.suntimes.getShutOffTime()

    else:
        pass
    time.sleep(600)

