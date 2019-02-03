# mike
# 18 November 2018

import piLibe.relay
import piLibe.suntimes
import piLibe.button
import time
import RPi.GPIO as GPIO

#=====================================
# initializations
#=====================================

relayChannel = 24
buttonChannel = 25

piLibe.relay.initRelay( relayChannel )
piLibe.button.initButton( buttonChannel )

#=====================================
# load the button callback
#=====================================

def turnOffLamp( buttonChannel ):
    piLibe.relay.disable( relayChannel )

piLibe.button.addCallback( buttonChannel, turnOffLamp )

#=====================================
# main
#=====================================

# boot-time test
piLibe.relay.enable( relayChannel )

while True:
    
    piLibe.utils.logger.simpleLog( "==TICK== sunrise.py" )

    if( piLibe.suntimes.isSunOut() ):
        piLibe.relay.enable( relayChannel )
    else:
        piLibe.relay.disable( relayChannel )
        
    time.sleep(600)
