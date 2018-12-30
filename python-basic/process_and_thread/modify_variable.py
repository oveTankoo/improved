# author: adam
import time, threading

local_balance = threading.local()

def change_it(n):
	blc = local_balance.balance
	blc += n
	blc -= n
	if blc != 0:
		print(blc)

def run_thread(n):
	local_balance.balance = 0
	for i in range(100000):
		#time.sleep(0.001)
		change_it(n)

t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))

t1.start()
t2.start()
t1.join()
t2.join()
#print(local_balance)