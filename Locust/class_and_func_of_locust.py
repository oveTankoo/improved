# coding: utf-8
# author: adam
# 主题：学习locust提供了哪些类和方法，它们分别实现了什么操作。

from locust import HttpLocust, TaskSet, task

class UserTask(TaskSet):
	@task
	def tc_index(self):
		self.client.get("/")

# 每一个模拟的用户，可以看做一个HttpLocust类的实例，HttpLocust类有以下属性：
class UserOne(HttpLocust):
	# 指向一个TaskSet类，TaskSet类定义了每个用户的行为
	task_set = UserTask
	# 一个Locust实例被挑选执行的权重，数值越大，执行频率越高
	weight = 1
	min_wait = 1000
	max_wait = 3000
	# 设置locust多少秒后超时，如果为None，则不会超时
	stop_timeout = 5
	# 相当于提供URL前缀的默认值，如果在命令行指定了--host，则以命令中的为准
	host = "https://www.baidu.com"

class UserTwo(HttpLocust):
	weight = 2
	task_set = UserTask
	host = "https://www.baidu.com"