# coding: utf-8
# author: adam
# 主题：简单介绍登录用户名、密码的参数化
from locust import HttpLocust, TaskSet, task
import random

class UserBehavior(Taskset):

	def on_start(self):
		# 调用登录函数进行登录
		self.login()

	# 随机返回登录用户
	def login_user():
		users = {"user1":"111111", "user2":"222222", "user3":"333333"}
		# 断言users对象为Dict，且非空
		assert isinstance(users, dict) and users != None
		# 先得到字典的Items对象，并转为List类型，随机获取一项
		user, pwd = random.choice(list(users.items()))
		return user, pwd

	@task
	def login(self):
		user, pwd = login_user()
		self.client.post("/login_action", {"user":user, "pwd":pwd})

class User(HttpLocust):
	task_set = UserBehavior
	min_wait = 1000
	max_wait = 3000
	host = "http://www.xxx.com"