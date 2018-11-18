# mike
# 17 November 2018

import RPi.GPIO as GPIO
import time
import ephem
import datetime

#=====================================
# Generic GPIO stuff
#=====================================

inChannels = [23]
outChannels = [24]
GPIO.setmode(GPIO.BCM)

for i in inChannels:
    GPIO.setup( i, GPIO.IN )

for i in outChannels:
    GPIO.setup( i, GPIO.OUT )
    GPIO.output( i, GPIO.HIGH )

#=====================================
# little library
#=====================================

# valve solenoid function
def dispenseWater():
    return False

# soil hygrometer functions
# try to water the plant for 30 seconds,
# then give up if it's not working
def callbackhelper( channel ):
    callback( channel, 0 )

def callback( channel, attempt ):
    if( attempt > 5 ):
        print( "I must be out of water. Stopping." )
    elif GPIO.input( channel ):
        print( "No water detected! Remedying...")
        dispenseWater()
        attempt += 1
        time.sleep( 5 )
        callback( channel, attempt )
    else:
        print( "Water detected!" )

def openBlinds():
    GPIO.output( 24, GPIO.LOW )
    print( "Opening Blinds" )
    time.sleep( 5 )
    GPIO.output( 24, GPIO.HIGH )

def closeBlinds():
    # GPIO.output( 24, GPIO.LOW )
    print( "Trying to Close Blinds" )
    time.sleep( 5 )
    print( "Failed to Close Blinds" )
    GPIO.output( 24, GPIO.HIGH )

def isSunrise( sunrise ):
    now = somewhere.date.tuple()
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
    now = somewhere.date.tuple()
    setting = sunset.tuple()
    arg1a = now[4]
    arg1b = setting[4]
    if( arg1a >= arg1b ):
        arg2a = now[5]
        arg2b = setting[5]
        if( arg2a >= arg2b ):
            return True
    return False

#=====================================
# add callback function to hygrometer
#=====================================

GPIO.add_event_detect( 23, GPIO.BOTH, bouncetime=300 ) # alert when change btwn high/low
GPIO.add_event_callback( 23, callbackhelper ) # run callback on change

#=====================================
# calculate sun times
#=====================================

somewhere = ephem.Observer()
somewhere.lat = '38.9717'
somewhere.lon = '-95.2353'
somewhere.elevation = 866
sun = ephem.Sun()

rising = somewhere.next_rising( sun )
setting = somewhere.next_setting( sun )

#=====================================
# main
#=====================================

while True:
    if( isSunrise( rising ) ):
        openBlinds()
        rising = somewhere.next_rising( sun )
    elif( isSunset( setting ) ):
        closeBlinds()
        setting = somewhere.next_rising( sun )
    else:
        pass
    time.sleep(5)

