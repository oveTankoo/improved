# 主题：使用多线程实现多人洗盘子->烘盘子的事情
import threading, queue
import time, random

def washer(dishes, dish_queue):
	for dish in dishes:
		print("%s am washing %s dish.\n"%(threading.current_thread().name, dish))
		time.sleep(1)	#洗盘子耗时1S
		dish_queue.put(dish)

def dryer(dish_queue):
	try:
		while True:
			# 接收队列中的事物，超时时间为1S
			dish = dish_queue.get(timeout = 1)
			print("%s am drying %s dish.\n"%(threading.current_thread().name, dish))
			time.sleep(0.5)		#烘盘子耗时0.5S
			dish_queue.task_done()
	except queue.Empty:
		pass	#直接忽略

dish_queue = queue.Queue()
for n in range(1,5):
	# 创建的线程名称默认为Thraed-1、Thraed-2等
	dryer_thread = threading.Thread(target = dryer, args = (dish_queue,))	#创建一个线程
	dryer_thread.start()	#激活线程

dishes = ['salad', 'bread', 'entree', 'desert']
# 洗盘子的人开始工作
washer(dishes, dish_queue)
# 等待所有人做完洗-烘盘子的活，任务结束（关闭所有线程）
dish_queue.join()