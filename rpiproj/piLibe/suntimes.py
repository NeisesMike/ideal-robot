# mike
# 18 november 2018

import ephem

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
    now = getDate().tuple()
    rise = sunrise.tuple()
    arg1a = now[4]
    arg1b = rise[4]
    if( arg1a >= arg1b ):
        arg2a = now[5]
        arg2b = rise[5]
        if( arg2a >= arg2b ):
            return True
    return False

def isSunset( sunset ):
    now = getDate().tuple()
    setting = sunset.tuple()
    arg1a = now[4]
    arg1b = setting[4]
    if( arg1a >= arg1b ):
        arg2a = now[5]
        arg2b = setting[5]
        if( arg2a >= arg2b ):
            return True
    return False
