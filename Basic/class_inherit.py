#定义一个“Animal”类，具有吃、喝、拉、撒的功能
class Animal(object):
	"""description for Animal"""
	#def __init__(self,name):
	#	self.name = name

	def eat(self):
		print('%s 吃'%self.name)

	def drink(self):
		print('%s 喝'%self.name)
	
	def shit(self):
		print('%s 拉'%self.name)	

	def pee(self):
		print('%s 撒'%self.name)	

class Cat(Animal):
	"""description for Cat"""
	def __init__(self,name):
		self.name = name
		self.bread = '猫'

	def cry(self):
		print('喵喵叫')

class Dog(Animal):
	"""description for Dog"""
	def __init__(self,name):
		self.name = name
		self.bread = '狗'

	def cry(self):
		print('汪汪叫')

if __name__ == '__main__':
	c1 = Cat('小白家的小黑猫')		#类Cat的一个实例c1
	c1.eat()	#实例调用方法eat()

	d1 = Dog('小黑家的小黄狗')
	d1.cry()