import time
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit

mh = Adafruit_MotorHAT(addr=0x60)
delay=0.15
class Car():
	def __init__(self,speed=0):
		self.speed=speed
		self.Left = mh.getMotor(1)
		self.Right = mh.getMotor(2)
		self.setSpeed(self.speed)
		atexit.register(self.stop)
	def forward(self):
		self.Left.run(Adafruit_MotorHAT.FORWARD)
		self.Right.run(Adafruit_MotorHAT.FORWARD)
	def reverse(self):
		self.Left.run(Adafruit_MotorHAT.BACKWARD)
		self.Right.run(Adafruit_MotorHAT.BACKWARD)
	def stop(self):
		self.Left.run(Adafruit_MotorHAT.RELEASE)
		self.Right.run(Adafruit_MotorHAT.RELEASE)
	def setSpeed(self,speed):
		self.speed=speed
		self.Left.setSpeed(int(speed*1.04))
		self.Right.setSpeed(speed)
	def left(self):
		self.Left.run(Adafruit_MotorHAT.BACKWARD)
		self.Right.run(Adafruit_MotorHAT.FORWARD)
		time.sleep(delay)
		self.Left.run(Adafruit_MotorHAT.FORWARD)
	def right(self):
		self.Right.run(Adafruit_MotorHAT.BACKWARD)
		self.Left.run(Adafruit_MotorHAT.FORWARD)
		time.sleep(delay)
		self.Right.run(Adafruit_MotorHAT.FORWARD)
###TESTING

#car =Car(100)
#car.forward()
#time.sleep(3)
#car.left()
#time.sleep(2)
#car.stop()
