# coding: utf-8
# author: adam
# subject: To do assert reponse.
from locust import HttpLocust, TaskSet, task

class UserTask(TaskSet):

	@task
	def job(self):
		with self.client.get("/", catch_response = True) as response:
			if response.status_code == 200:
				response.failure("Request failed !")
			else:
				response.sucsess()

class User(HttpLocust):
	task_set = UserTask
	min_wait = 1000# ms
	max_wait = 3000# ms
	host = "https://www.baidu.com"