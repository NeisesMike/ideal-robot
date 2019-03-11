# mike
# 11 March 2019

import piLibe.relay
import piLibe.suntimes
import time
import RPi.GPIO as GPIO
import piLibe.utils.logger

#=====================================
# initializations
#=====================================

plantRelayChannel = 24

piLibe.relay.initRelay( plantRelayChannel )

#=====================================
# main
#=====================================

# boot-time tests
piLibe.relay.enableFor( plantRelayChannel, 1 )

while True:
    
    piLibe.utils.logger.simpleLog( "==TICK== garden" )

    if( piLibe.suntimes.isLampTime() ):
        piLibe.relay.enable( plantRelayChannel )
    else:
        piLibe.relay.disable( plantRelayChannel )

    time.sleep(3600)

