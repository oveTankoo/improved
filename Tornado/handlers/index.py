#coding=utf-8
import tornado.web

#当访问根目录时，就将相应的请求交给handler目录中index.py的IndexHandler类的get()来处理
#它的处理结果就是，呈现index.html模板内容
class IndexHandler(tornado.web.RequestHandler):
	"""docstring for IndexHandler"""
	def get(self):
		#render()在于向请求者反馈网页模板
		self.render("index.html")