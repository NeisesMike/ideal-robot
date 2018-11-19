# mike
# 18 november 2018

import ephem
import datetime

Lawrence = ephem.Observer()
Lawrence.lat = '38.9717'
Lawrence.lon = '-95.2353'
Lawrence.elevation = 866

sun = ephem.Sun()

def getDate():
    return( Lawrence.date )

def getSunrise():
    return( Lawrence.next_rising( sun ) )

def getSunset():
    return( Lawrence.next_setting( sun ) )

def isSunrise( sunrise ):
    return( getDate() >= sunrise )

def isSunset( sunset ):
    return( getDate() >= sunset )

# INPUT ephem.Date
# OUTPUT python datetime
def getShutOffTime( sunrise ):
    return( ephem.localtime( sunrise ) + datetime.timedelta( hours=12 ) )

# INPUT python datetime
def isShutOffTime( shutoff ):
    return( shutoff < datetime.datetime.now() )

