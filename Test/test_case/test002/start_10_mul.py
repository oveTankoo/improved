# author: adam
import unittest
import time

class MathHandle(unittest.TestCase):
	def setUp(self):
		pass

	def test_001_mul_something(self):
		"""进行加法运算，但有时间间隔"""
		total = 1
		for x in range(1,10):
			total = total * x
			time.sleep(1)
		print("总乘积: %s"%total)

	def tearDown(self):
		pass

if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(MathHandle('test_001_mul_something'))
	runer = unittest.TextTestRunner()
	runer.run(suite)