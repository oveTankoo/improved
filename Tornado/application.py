#coding:utf-8
"""完成对网站系统的基本配置，建立网站的请求处理集合"""
from url import url

import tornado.web
import os

#引用字典对象，约定了模板和静态文件的路径
settings = dict(
	template_path = os.path.join(os.path.dirname(__file__),'templates'),
	static_path = os.path.join(os.path.dirname(__file__),'statics')
	)

#请求处理集合对象
application = tornado.web.Application(
	handlers = url,
	**settings
	)