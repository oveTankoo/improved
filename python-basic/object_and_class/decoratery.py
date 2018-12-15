# 调试类里面的装饰器
# edited:adam
# 
def handle(func):
		def new_func(self, *args, **kargs):
			self._init()
			print('The function name is:', func.__name__)
			print('The positional args is:', args)
			print('The keryvalues args is:', kargs)
			result = func(self, *args, **kargs)
			self._end()
			return result
		return new_func

class Help(object):
	"""docstring for Help"""
	def _init(self):
		print('We are to start !')

	def _end(self):
		print('We are to end !')

	@handle
	def example(self):
		print('I comming !')

if __name__ == '__main__':
	Help = Help().example()