# mike
# 19 november 2018

import sys
import Adafruit_DHT
import utils.logger

def getHumidity( channel ):
    humidity, temperature = Adafruit_DHT.read_retry( 11, channel )
    utils.logger.simpleLog( "Humidity is: {}".format(humidity) )
    return( humidity )

def getTemp( channel ):
    humidity, temperature = Adafruit_DHT.read_retry( 11, channel )
    utils.logger.simpleLog( "Temperature is: {}".format(temperature) )
    return( temperature )

