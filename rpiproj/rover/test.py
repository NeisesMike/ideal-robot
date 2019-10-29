#!/usr/bin/python3

from picar import back_wheels, front_wheels
#from .driver import camera, stream
import picar
import time

# boilerplate stuff
picar.setup()
db_file = "/home/pi/SunFounder_PiCar-V/remote_control/remote_control/driver/config"
fw = front_wheels.Front_Wheels(debug=False, db=db_file)
bw = back_wheels.Back_Wheels(debug=False, db=db_file)
#cam = camera.Camera(debug=False, db=db_file)

fw.ready()
bw.ready()
#cam.ready()

SPEED = 75
bw_status = 0

# library stuff
def carStop():
    bw.forward()
    fw.turn_straight()
    time.sleep(.1)
    bw.stop()

# turn around
bw.speed = SPEED
fw.turn_right()
bw.forward()
time.sleep(1) 
fw.turn_straight()
time.sleep(1) 
fw.turn_left()
time.sleep(2) 
carStop()

print( "done!" )

