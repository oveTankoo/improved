# task_master.py
# coding: utf-8
import queue, random, time
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 自定义函数re_task_queue(用来返回task_queue对象)
def re_task_queue():
	global task_queue
	return task_queue

# 自定义函数re_result_queue(用来返回result_queue对象)
def re_result_queue():
	global result_queue
	return result_queue

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
	pass
	
if __name__ == '__main__':	
	# 把2个Queue都注册到网络上，callable参数关联了Queue对象：
	QueueManager.register('get_task_queue', callable = re_task_queue)#lambda: 
	QueueManager.register('get_result_queue', callable = re_result_queue)#lambda:
	# 绑定 master 主机端口5000，设置验证码“abc”
	manager = QueueManager(address = ('192.168.1.101',5000), authkey = b'abc')
	# 启动Queue:
	manager.start()
	
	# 获得通过网络访问的Queue对象:
	task = manager.get_task_queue()
	result = manager.get_result_queue()
	
	# 放几个任务进去:
	for i in range(10):
		print('Put task %d...'%i)
		task.put(i)
	
	# 从result队列读取结果(设置等待时间为100s):
	print('Try to get results...')
	for i in range(10):
		r = result.get(timeout = 100)
		print('Result: %s'%r)
	
	# 关闭
	manager.shutdown()
	print('master exit.')	