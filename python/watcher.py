#!/usr/bin/python
import time
from Car import Car
import os

car = Car(0)

directions={
	"FORWARD":car.forward,
	"REVERSE":car.reverse,
	"STOP":car.stop,
	"RIGHT":car.right,
	"LEFT":car.left
}

dt=os.stat("/home/pi/sacredsf-projects/car/direction.txt").st_mtime

while(True):
	poll=os.stat("/home/pi/sacredsf-projects/car/direction.txt").st_mtime

	fd = open("/home/pi/sacredsf-projects/car/direction.txt",'rw')
	direction=fd.read()
	if(poll == dt and (direction=="LEFT" or direction=="RIGHT")):
		#no change, so just go forward
		direction = "FORWARD"
	if(poll!=dt):
		dt=poll
	direction=direction.strip()
	sh=open("/home/pi/sacredsf-projects/car/speed.txt")
	speed = int(sh.read())
	car.setSpeed(speed)
	try:
	
		func=directions[direction]
		func()
	except(KeyError):
		print("KEY ERROR")
#	if(direction!="FORWARD" and direction!="REVERSE"):
	
	fd.close()
	time.sleep(0.0001)

