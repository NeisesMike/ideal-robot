#!/usr/bin/python
import ephem
import datetime

somewhere = ephem.Observer()
somewhere.lat = '38.9717'
somewhere.lon = '-95.2353'
somewhere.elevation = 866
print somewhere.date

sun = ephem.Sun()
r1 = somewhere.next_rising(sun)
s1 = somewhere.next_setting(sun)

somewhere.horizon = '0:34'
r2 = somewhere.next_rising(sun)
s2 = somewhere.next_setting(sun)
print( "visual sunrise %s" % r1 )
print( "visual sunset %s" % s1 )
print( "naval obs sunrise %s" % r2 )
print( "naval obs sunset %s" % s2 )

print( r2.tuple() )

print( somewhere.date.tuple() )
