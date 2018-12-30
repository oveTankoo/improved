# author: adam
# 主题：用进程池（Pool）的方式批量创建子进程
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print("Run task %s (%s)..."%(name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 2)
	end = time.time()
	print("Task %s run %0.2f seconds."%(name, (end - start)))

if __name__ == '__main__':
	print("Parent process %s has run."%os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args = (i,))
	print("Waiting for all subprocesses done...")
	p.close()
	p.join()
	print("All process done.")