# author: adam
import unittest
import time

class MathHandle(unittest.TestCase):
	def setUp(self):
		pass

	def test_001_sum_something(self):
		"""进行加法运算，但有时间间隔"""
		total = 0
		for x in range(1000):
			total = total + x
			time.sleep(0.01)
		print("总和: %s"%total)

	def tearDown(self):
		pass

if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(MathHandle('test_001_sum_something'))
	runer = unittest.TextTestRunner()
	runer.run(suite)