# mike
# 18 November 2018

import piLibe.relay
import piLibe.solenoidValve
import piLibe.dht
import time
import RPi.GPIO as GPIO

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
    if( piLibe.dht.getHumidity( dhtChannel ) < 40.0 ):
        piLibe.relay.enable( relayChannel )
        while( piLibe.dht.getHumidity( dhtChannel ) < 70.0 ):
            print( piLibe.dht.getHumidity( dhtChannel ) )
            time.sleep( 10 )
        piLibe.relay.disable( relayChannel )
        piLibe.solenoidValve.openFor( valveChannel, 15 )
    time.sleep(600)

