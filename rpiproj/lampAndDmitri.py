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

hygrometerChannel = 22
valveChannel = 23
plantRelayChannel = 24
dmitriRelayChannel = 25

piLibe.solenoidValve.initValve( valveChannel )
piLibe.hygrometer.initHygrometer( hygrometerChannel )
piLibe.relay.initRelay( plantRelayChannel )
piLibe.relay.initRelay( dmitriRelayChannel )

#=====================================
# load the hygrometer callback
#=====================================

def dispenseWater( valveChannel, hygroChannel, attempt ):
    if( attempt > 3 ):
        print( "I must be out of water. Stopping." )
        piLibe.utils.logger.simpleLog( "VALVE ON CHANNEL {} IS OUT OF WATER".format(valveChannel) )
    elif( piLibe.hygrometer.isWater(hygroChannel) ):
        print( "Water detected!" )
        piLibe.solenoidValve.close( valveChannel )
    else:
        print( "No water detected! Remedying...")
        piLibe.solenoidValve.open( valveChannel )
        time.sleep( 10 )
        attempt += 1
        dispenseWater( valveChannel, hygroChannel, attempt )

def tryWater( channel ):
    dispenseWater( valveChannel, hygrometerChannel, 0 )

piLibe.hygrometer.addCallback( hygrometerChannel, tryWater )

#=====================================
# main
#=====================================

# boot-time tests
piLibe.relay.enableFor( plantRelayChannel, 1 )
piLibe.relay.enableFor( dmitriRelayChannel, 1 )

while True:
    
    piLibe.utils.logger.simpleLog( "==TICK== lampAndDmitri.py" )

    if( piLibe.suntimes.isSunOut() ):
        piLibe.relay.enable( dmitriRelayChannel )
    else:
        piLibe.relay.disable( dmitriRelayChannel )
        
    if( piLibe.suntimes.isLampTime() ):
        piLibe.relay.enable( plantRelayChannel )
    else:
        piLibe.relay.disable( plantRelayChannel )

    time.sleep(600)

