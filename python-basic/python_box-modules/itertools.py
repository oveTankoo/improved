import itertools
lis1 = [1,2,3,4]
lis2 = ['a','b','c','d']

for item in itertools.chain(lis1, lis2):
	print(item)

print('\n')

# accumulate()计算累积的值。默认的话，计算的是累积和；
for item in itertools.accumulate(lis1):
	print(item)

print('\n')

# 可以把一个函数作为accumulate()的第二个参数，代替默认的加法；
def multiply(a, b):
	return a * b

for item in itertools.accumulate(lis1, multiply):
	print(item)

# itertools模块有很多其他的函数，可以用在需要节省时间的组合和排列问题上。