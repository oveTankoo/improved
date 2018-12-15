# deque是一种双端队列，同时具有栈和队列的特征。
# 它可以从序列的任何一端进行添加和删除某项
# 应用举例：从一个词的两端扫向中间，判断是否为回文。
from collections import deque

def palindrome(word):
	dq = deque(word)
	#print(dir(dq),'\n')
	while len(dq) > 1:
		# 比较左右删除方法得到的值，是否相等？
		if dq.popleft() != dq.pop():
			return False
	return True

result = palindrome('wan')

print(result,'\n')

# python 没有对字符串进行反转的函数，但可以利用反向切片的方法
# 快速判断字符串，是否为回文的方法（参考）
def quick_func(word):
	return word == word[::-1]

quick = quick_func('word')
print(quick)