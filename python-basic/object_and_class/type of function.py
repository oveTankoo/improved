# coding: utf-8
# author: adam

class Example(object):
	"""docstring for Example"""
	count = 0

	def __init__(self):
		"""初始化方法，使类属性值加1
		此处Example.count 与 self.count，意义不同"""
		Example.count += 1

	def instance_func(self):
		"""实例方法:
		当它被调用时，Python会把调用该方法的对象作为self参数传入"""
		print('The value of "count" is %d currently.'%self.count)

	@classmethod
	def class_func(cls):
		"""类方法:
		作用于整个类，对类作出的任何改变会对它的所有实例对象产生影响，其中cls.count与Example.count作用一样"""
		print('Example has', cls.count, 'little objects.')

	@staticmethod
	def static_func():
		"""静态方法:
		既不会影响类，也不会影响类的实例对象，出现在类中仅仅为了方便"""
		print('I am using a static function.')

if __name__ == '__main__':
	e1 = Example()
	e1.instance_func()
	e1.class_func()
	e1.static_func()

	# 创建新的对象，此时类方法的 cls.count 能体现类属性的改变
	e2 = Example()
	e2.class_func()