# coding = utf-8
# 主题：使用多进程实现多人洗盘子->烘盘子的事情
import multiprocessing as mp

def washer(dishes, output):
	for dish in dishes:
		print('I am washing %s dish'%dish)
		output.put(dish)

def dryer(input):
	while True:
		dish = input.get(timeout = 10)
		print('I am drying %s dish'%dish)
		input.task_done()

if __name__ == '__main__':
	dish_queue = mp.JoinableQueue()
	#
	dryer_proc = mp.Process(target = dryer, args = (dish_queue,))
	dryer_proc.daemon = True
	dryer_proc.start()

	dishes = ['salad', 'bread', 'entree', 'desert']
	washer(dishes, dish_queue)
	dish_queue.join()
	#dryer_proc.join()
	#mp.freeze_support()