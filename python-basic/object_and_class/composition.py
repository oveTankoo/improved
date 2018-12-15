# author: adam
# 当想要创建的对象X，与Y是父类和子类的关系（is-a），与Z是包含的关系（has-a）
# 这时使用组合（composition）或者聚合（aggregation）的方式，更符合现实的逻辑
# 
class Bill():
	def __init__(self, description):
		self.description = description

class Tail():
	def __init__(self, length):
		self.length = length

class Duck():
	def __init__(self, bill, tail):
		self.bill = bill
		self.tail = tail

	def about(self):
		print('this duck has a %s bill and a %s tail'%(bill.description, tail.length))

bill = Bill('wide orange')	#实例化类Bill，得到对象bill，并有 description 属性
tail = Tail('long')			#实例化类Tail，得到对象tail，并有 length 属性

duck = Duck(bill, tail)		#将2个对象作为参数传入，并实例化类Duck
duck.about()				#调用想实现的方法