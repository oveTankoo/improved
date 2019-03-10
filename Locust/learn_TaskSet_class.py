# coding: utf-8
# author: adam
# 主题：TaskSet类定义了每个用户的任务集合，测试任务开始后，每个locust用户会从TaskSet中随机挑选一个任务执行，
# 然后随机等待定义的min_wait与max_wait之间的一段时间，执行下一个任务

from locust import HttpLocust, TaskSet, task

class stay(TaskSet):

	def on_stay(self):
		"""on_stay is called when a locust start before any task is scheduled."""
		print("start test.")

	@task(3)
	def readBook(self):
		print("I am reading a book.")

	@task(6)
	def listenMusic(self):
		print("I am listening a music.")

	@task(1)
	def logout(self):
		self.interrupt()