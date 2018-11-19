# mike
# 19 november 2018

import sys
import Adafruit_DHT

def getHumidity( channel ):
    humidity, temperature = Adafruit_DHT.read_retry( 11, channel )
    return( humidity )

def getTemp( channel ):
    humidity, temperature = Adafruit_DHT.read_retry( 11, channel )
    return( temperature )

