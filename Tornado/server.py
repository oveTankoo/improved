#coding:utf-8
"""将tornado服务器运行起来，并且囊括前面2个文件中得到对象属性设置"""

import tornado.ioloop
import tornado.options
import tornado.httpserver

from application import application
from tornado.options import define,options

define('port',default=8000,help='run on the given port',type=int)

def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(options.port)
	#开启服务器
	tornado.ioloop.IOLoop.instance().start()
	print("Development server is running at http://127.0.0.1:%s"%options.port)
	print("Quit the server with Ctrl-C")

if __name__ == '__main__':
	main()