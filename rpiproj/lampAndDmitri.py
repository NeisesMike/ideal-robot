# mike
# 19 November 2018

import piLibe.hygrometer
import piLibe.relay
import piLibe.solenoidValve
import piLibe.suntimes
import time
import RPi.GPIO as GPIO
import piLibe.utils.logger

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
    
    piLibe.utils.logger.simpleLog( "TICK lampAndDmitri.py" )

    if( piLibe.suntimes.isSunOut() ):
        piLibe.relay.enable( dmitriRelayChannel )
    else:
        piLibe.relay.disable( dmitriRelayChannel )
        
    if( piLibe.suntimes.isLampTime() ):
        piLibe.relay.enable( plantRelayChannel )
    else:
        piLibe.relay.disable( plantRelayChannel )

    time.sleep(60)

