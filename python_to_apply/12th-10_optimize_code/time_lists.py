"""
主题：通过timeit.timeit比较2种不同算法的快慢。
"""
from timeit import timeit

def build_list_1():
	wanted = []
	for x in range(1000):
		wanted.append(x)
	return wanted

def build_list_2():
	wanted = [value for value in range(1000)]
	return wanted

print('build_list_1 takes', timeit(build_list_1, number = 1000), 'seconds')
print('build_list_2 takes', timeit(build_list_2, number = 1000), 'seconds')