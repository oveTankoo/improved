# python对那些需要刻意隐藏在类内部的特性有自己的命名规范：
# 由2个连续的下划线开头（__）
# 这种命名规范本质上并没有把特性变成私有，但python确实把它的名字重整了，
# 让外部代码无法使用

class Duck(object):
	"""docstring for Duck"""
	def __init__(self, input_name):
		self.__name = input_name
		
	@property
	def name(self):
		print('inside the getter')
		return self.__name

	@name.setter
	def name(self, input_name):
		print('inside the setter')
		self.__name = input_name

fowl = Duck('Howard')
print(fowl.name)

fowl.name = 'Donald'
print(fowl.name)

# 使用技巧获取特性__name
print(fowl._Duck__name)

# 使用一般方法去获取特性__name(报错)
print(fowl.__name)