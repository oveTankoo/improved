# coding: utf-8
# author: adam
# 主题：自己实践，创建2种不同请求任务，并1:2分配用户去执行
from locust import HttpLocust, TaskSet, task

class behaviorOne(TaskSet):

	def on_start(self):
		print("To request index.")

	@task
	def req_index(self):
		self.client.get("/")

class behaviorTwo(TaskSet):

	def on_start(self):
		print("To request query.")

	@task
	def req_query(self):
		self.client.get("?wd=python")

class UserOne(HttpLocust):
	task_set = behaviorOne# 选择要执行的任务
	weight = 1# 执行权重 - 决定最终分配到执行任务的人数
	min_wait = 1000
	max_wait = 3000
	host = "https://www.baidu.com"

class UserTwo(HttpLocust):
	task_set = behaviorTwo
	weight = 2# 执行权重 - 执行behaviorTwo的人是执行behaviorOne的2倍
	min_wait = 1000
	max_wait = 2000
	host = "https://www.baidu.com"