# 1.Inherit in class
class Car(object):
	"""docstring for Car"""
	def exclaim(self):
		print("I'am a car !\n")

class Yugo(Car):
	pass

car001 = Car()
yugo001 = Yugo()

car001.exclaim()
yugo001.exclaim()

# 2.Override in class
class Car(object):
	"""docstring for Car"""
	def exclaim(self):
		print("I'am a car !")

class Yugo(Car):
	"""docstring for Yugo"""
	def exclaim(self):
		print("I'am a Yugo! Much lick a car , but more Yugo-ish.\n")

car002 = Car()
yugo002 = Yugo()

car002.exclaim()
yugo002.exclaim()

# 3.Use 'super' to gain help of super class
class Person():
	"""docstring for Person"""
	def __init__(self, name):
		self.name = name

# 子类Sender定义了__init__()方法时，父类的__init_()方法会被覆盖，因此我们必须显示调用它
class Sender(Person):
	"""docstring for Sender"""
	def __init__(self, name, email):
		super().__init__(name)
		self.email = email

adam = Sender('adam','123@abc.com')
print(adam.name)
print(adam.email)