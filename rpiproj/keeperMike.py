# mike
# 18 November 2018

import piLibe.relay
import piLibe.button
import datetime
import time
import RPi.GPIO as GPIO

#=====================================
# initializations
#=====================================

relayChannel = 24
buttonChannel = 25

piLibe.relay.initRelay( relayChannel )
piLibe.button.initButton( buttonChannel )

eightAM = datetime.time( 8,0,0 )

def is0800():
    return( datetime.datetime.now().time() > eightAM )

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

    if( is0800() ):
        piLibe.relay.enable( relayChannel )
        
    time.sleep(600)
