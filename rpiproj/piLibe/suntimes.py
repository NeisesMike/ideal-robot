# mike
# 19 november 2018

import ephem
import datetime

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

def hasSunRisen( sunrise ):
    return( getDate() >= sunrise )

def hasSunSet( sunset ):
    return( getDate() >= sunset )

# -12 degrees for nautical twilight
def isSunOut():
    s = ephem.Sun()
    larry = ephem.city( 'Houston' )
    s.compute( larry )
    twilight = -12 * ephem.degree
    return( s.alt > twilight )

def isLampTime():
    now = getDate()
    lastRise = getLastSunrise()
    shutoff = ephem.Date( lastRise + 12*ephem.hour )
    return( lastRise < now and now < shutoff )

print( "sun's out" if isSunOut() else "sun's down" )
print( getDate() )
print( getSunset() )
print( "lamp's on" if isLampTime() else "lamp's off" )
