# mike
# 18 November 2018

import piLibe.relay
import piLibe.suntimes
import time
import RPi.GPIO as GPIO

#=====================================
# initializations
#=====================================

relayChannel = 24
buttonChannel = 25

piLibe.relay.initRelay( relayChannel )
piLibe.button.initButton( buttonChannel )

rising = piLibe.suntimes.getSunrise() 
shutoff = piLibe.suntimes.getShutOffTime( rising )

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
    if( piLibe.suntimes.isSunrise( rising ) ):
        piLibe.relay.enable( relayChannel )
        rising = piLibe.suntimes.getSunrise()
    elif( piLibe.suntimes.isShutOffTime( shutoff ) ):
        piLibe.relay.disable( relayChannel )
        shutoff = piLibe.suntimes.getShutOffTime()
    else:
        pass
    time.sleep(600)

