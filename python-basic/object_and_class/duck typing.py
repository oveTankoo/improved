# coding: utf-8
# author: adam
# content: duck typing
class Quote(object):
	"""docstring for Quote"""
	def __init__(self, person, words):
		self.person = person
		self.words = words
	
	def who(self):
		return self.person

	def says(self):
		return self.words + '.'

# 以下的2个类继承Quote，并沿用 __init__()，即创建实例对象时要传入初始值
class QuestionQuote(Quote):
	def says(self):
		return self.words + '?'

class ExclamationQuote(Quote):
	def says(self):
		return self.words + '!'

# 接下来创建一些对象
hunter = Quote('Adam', "I'm hunting tiger")
print(hunter.who(), 'says:', hunter.says())

hunter1 = QuestionQuote('James', "What's up,man")
print(hunter1.who(), 'says:', hunter1.says())

hunter2 = ExclamationQuote('Hardon', "I'm a great man")
print(hunter2.who(), 'says:', hunter2.says(), '\n')

# 3个不同版本的says()为3个类提供不同的响应方式，这是面向对象语言中多态的传统形式
# python在这方面走的更远一些，无论对象的种类是什么，只要包含who()和says()，你便可以调用它
# 再定义一个 BabblingBrook 类，它与Quote类的后代没有任何关系，这种方式被称为“鸭子类型”

class BabblingBrook():
	def who(self):
		return 'Brook'
	def says(self):
		return 'Babble'
brook = BabblingBrook()		#实例化BabblingBrook类

def who_says(obj):
	print(obj.who(), 'says:', obj.says())

who_says(hunter)
who_says(hunter1)
who_says(brook)