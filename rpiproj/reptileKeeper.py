# mike
# 18 November 2018

import piLibe.relay
import piLibe.solenoidValve
import piLibe.dht
import time
import RPi.GPIO as GPIO
import piLibe.utils.logger

#=====================================
# initializations
#=====================================

dhtChannel = 23
relayChannel = 24
valveChannel = 25

piLibe.relay.initRelay( relayChannel )
piLibe.solenoidValve.initValve( valveChannel )

#=====================================
# main
#=====================================

while True:
    print( "Ding! we're at {}% humidity!".format( piLibe.dht.getHumidity( dhtChannel ) ) )
    piLibe.utils.logger.simpleLog( "TICK reptileKeeper.py" )
    if( piLibe.dht.getHumidity( dhtChannel ) < 40.0 ):
        # turn on the atomizer
        piLibe.relay.enable( relayChannel )
        while( piLibe.dht.getHumidity( dhtChannel ) < 70.0 ):
            print( piLibe.dht.getHumidity( dhtChannel ) )
            time.sleep( 3 )
        # turn off the atomizer
        piLibe.relay.disable( relayChannel )
        # add some water to the reservoir
        piLibe.solenoidValve.openFor( valveChannel, 15 )
    time.sleep(600)

