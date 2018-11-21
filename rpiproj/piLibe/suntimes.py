# mike
# 19 november 2018

import ephem
import datetime
import math
import utils.logger

Lawrence = ephem.Observer()
Lawrence.lat = '38.9717'
Lawrence.lon = '-95.2353'
Lawrence.elevation = 866

def getDate():
    return( Lawrence.date )

def getSunrise():
    return( Lawrence.next_rising( ephem.Sun() ) )

def getLastSunrise():
    return( Lawrence.previous_rising( ephem.Sun() ) )

def getSunset():
    return( Lawrence.next_setting( ephem.Sun() ) )

def isSunOut():
    sunout = getSunset() < getSunrise()
    utils.logger.piLog( "sunlog", "sun's out" if sunout else "sun's down" )
    return( sunout )

def isLampTime():
    lampon = ( getDate() < ephem.Date( getLastSunrise() + 12 * ephem.hour ) )
    utils.logger.piLog( "lamplog", "lamp's on" if lampon else "lamp's off" )
    return( lampon )

