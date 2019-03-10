# 主题：
from locust import HttpLocust, TaskSet, task

# UserBehavior类继承TaskSet类，用于描述用户行为
class UserBehavior(TaskSet):

	@task
	def baidu_index(self):
		# 请求根目录
		self.client.get("/")

# websiteUser类，用于设置性能测试
class websiteUser(HttpLocust):
	# 指向一个定义的用户行为类
	task_set = UserBehavior
	# 执行事务之间用户的最小等待时间(ms)
	min_wait = 3000
	# 执行事务之间用户的最大等待时间
	max_wait = 6000