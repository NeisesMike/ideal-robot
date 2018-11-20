# mike
# 20 november 2018
import datetime

def sessionStart( filename ):
    now = datetime.datetime.now().replace(microsecond=0)
    with open( "/home/pi/{}".format(filename), "a" ) as f:
        f.write( "==============================\n{}: SESSION START\n".format(now) )

def piLog( filename, string ):
    now = datetime.datetime.now().replace(microsecond=0)
    with open( "/home/pi/{}".format(filename), "a" ) as f:
        f.write( "{time}: {msg}\n".format(time=now, msg=string ) )

def simpleLog(  string ):
    now = datetime.datetime.now().replace(microsecond=0)
    with open( "/home/pi/piLog", "a" ) as f:
        f.write( "{time}: {msg}\n".format( time=now, msg=string ) )

sessionStart( "piLog" )
