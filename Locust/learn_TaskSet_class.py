# coding: utf-8
# author: adam
# 主题：TaskSet类定义了每个用户的任务集合，测试任务开始后，每个locust用户会从TaskSet中随机挑选一个任务执行，
# 然后随机等待定义的min_wait与max_wait之间的一段时间，执行下一个任务
# Execute: locust -f learn_TaskSet_class.py --no-web -c 10 -r 10 -t 10
from locust import HttpLocust, TaskSet, task

class stay(TaskSet):

	# 定义每个用户开始做的第一件事
	def on_start(self):
		"""on_start is called when a locust start before any task is scheduled."""
		print("start test!")

	# 通过@task()装饰的方法为一个事务，参数越大则每次被虚拟用户执行的概率越高，默认值是1.
	@task(3)
	def readBook(self):
		print("I am reading a book.")

	@task(6)
	def listenMusic(self):
		print("I am listening a music.")

	@task(1)
	def logout(self):
		# 顶层的TaskSet不能调用这个方法。reschedule为True时，从被嵌套任务出来马上选择新任务执行.
		# 如果为False，从被嵌套任务出来后，随机等待min_wawit和max_wait之间的时间，开始执行新任务.
		self.interrupt(reschedule = True)

class UserTask(TaskSet):
	# 表示每个用户执行stay的频率是2，UserTask的2倍
	tasks = {stay:2}

	@task(1)
	def leave(self):
		#self.client.get("/")
		print("I don't like this page.")

class User(HttpLocust):
	task_set = UserTask
	host = "https://www.baidu.com"