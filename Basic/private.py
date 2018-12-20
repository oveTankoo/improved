#coding=utf-8

class Private(object):
	"""docstring for Private"""
	def __init__(self):
		self.value1 = 'hello'
		self.__value2 = 'world'

	def __protect(self):
		print('I am a protect func')
		#在类空间中，调用私有属性；
		print(self.value1 + ','+self.__value2)

	#如果要调用私有属性，可以用property函数
	@property
	def get_value(self):
		return self.__value2

	def signal(self):
		print('Then,call the private func!')
		#在类空间中，调用私有方法；
		self.__protect()
 
if __name__ == '__main__':
	p = Private()	#实例化类
	p.signal()		#通过实例，调用signal方法；
	print(p.get_value)	#用了@property之后，调用方法用的是instance.func_name的形式
	p.__protect()	#在类空间外（实例），无法调用私有方法（报错）；
	p.__value2	#在类空间外（实例），无法调用私有属性（报错）；