# author: adam
# 
class Laser():
	def does():
		return 'disintegrate'

class Claw():
	def does():
		return 'crush'

class SmartPhone():
	def does():
		return 'ring'

class Robot():
	def __init__(self, laser, claw, smart_phone):
		self.laser = laser
		self.claw = claw
		self.smart_phone = smart_phone

	def does(self):
		print('when the',self.smart_phone.does(),claw.dose(),'there are not ',laser.does())

laser = Laser()
claw = Claw()
smart_phone = SmartPhone()
print(smart_phone)

robot = Robot(laser, claw, smart_phone)
robot.does()