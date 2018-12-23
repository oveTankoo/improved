# coding: utf-8
import multiprocessing as mp
import time

def worker():
    name = mp.current_processs().name
    print(name,'is starting')
    time.sleep(2)
    print(name,'is exiting')

def my_service():
    name = mp.current_processs().name
    print(name,'is starting')
    time.sleep(2)
    print(name,'is exiting')

if __name__ == '__main__':
    service = mp.Process(name = 'my_service', target = my_service)
    worker_1 = mp.Process(name = 'worker_1', target = worker)
    worker_2 = mp.Process(name = 'worker_2', target = worker)

    worker_1.start()
    worker_2.start()
    service.start()