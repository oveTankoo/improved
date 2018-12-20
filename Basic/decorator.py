# coding: utf-8
# author: adveroo
# 本节主要涉及装饰器的规范和使用

# 函数document_it()定义了一个装饰器，去实现如下功能：
# ·打印函数的名字和参数的值
# ·执行含有参数的函数
# ·打印输出结果
# ·返回修改后的函数

def document_it(func):
	'''无论传入document_it()的函数func是什么，装饰器都会返回一个新的函数，
	其中包含函数document_it()增加的额外语句。'''
	def new_function(*args, **kargs):
		print('Running function:', func.__name__)
		print('Positional arguments:', args)
		print('Keyword arguments:', kargs)
		result = func(*args, **kargs)
		print('Result:', result)
		return result
	return new_function

# 那么如何使用装饰器呢？当然，可以通过人工赋值：
def add_func(a, b):
	return a + b

# 人工对装饰器赋值
cooler_add_func = document_it(add_func)
# 打印该对象的属性
print(type(cooler_add_func))
# 执行该对象-函数
cooler_add_func(3,5)
print('\n')

# 替代人工方法：在要装饰的函数前添加装饰器名字@decorator_name
@document_it
def add_func1(a, b):
	return a + b

add_func1(4, 6)

# ·同时，一个函数可以有多个装饰器，下面是一个对结果求平方的装饰器square_it():
def square_it(func):
	def new_function(*args, **kargs):
		result = func(*args, **kargs)
		return result * result
	return new_function

# · 靠近函数定义（def上面）的装饰器最先被执行，然后依次执行上面的。
# ·任何顺序都会得到相同的最终结果（观察2个例子中间的变化）

@document_it
@square_it
def add_func2(a, b):
	return a + b

@square_it
@document_it
def add_func3(a, b):
	return a + b

print(add_func2(3, 5))
print('\n')
print(add_func3(3, 5))