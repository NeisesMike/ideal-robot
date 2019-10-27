#!/usr/local/bin/python3

from picar import back_wheels, front_wheels
import picar
from time import sleep

# boilerplate stuff
db_file = "/home/pi/SunFounder_PiCar-V/remote_control/remote_control/driver/config"
fw = front_wheels.Front_Wheels(debug=False, db=db_file)
bw = back_wheels.Back_Wheels(debug=False, db=db_file)
cam = camera.Camera(debug=False, db=db_file)

fw.ready()
bw.ready()
cam.ready()

SPEED = 60
bw_status = 0

# turn around
bw.speed = SPEED
fw.turn_right()
bw.forward()
sleep(1) 
fw.turn_straight()
sleep(1) 
fw.turn_left()
sleep(2) 

print( "done!" )

