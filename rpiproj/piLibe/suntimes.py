# mike
# 19 november 2018

import ephem
import datetime
import math

Lawrence = ephem.Observer()
Lawrence.lat = '38.9717'
Lawrence.lon = '-95.2353'
Lawrence.elevation = 866

def getDate():
    Lawrence.date = ephem.now()
    return( Lawrence.date )

def getSunrise():
    return( Lawrence.next_rising( ephem.Sun() ) )

def getLastSunrise():
    return( Lawrence.previous_rising( ephem.Sun() ) )

def getSunset():
    return( Lawrence.next_setting( ephem.Sun() ) )

def isSunOut():
    Lawrence.date= ephem.now()
    return( getSunset() < getSunrise() )

def isLampTime():
    Lawrence.date= ephem.now()
    return( getDate() < ephem.Date( getLastSunrise() + 12 * ephem.hour ) )

