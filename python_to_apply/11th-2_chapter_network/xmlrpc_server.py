# author: adam
# 标准库中包含一种RPC实现，xmlrpc，使用XML作为传输格式。
# 在服务器上定义并注册函数，客户端使用类似导入的方式来调用它们。
from xmlrpc.server import SimpleXMLRPCServer
import math

# 定义函数
def double(num):
	return num * 2

def power(num):
	return math.pow(num, 2)

server = SimpleXMLRPCServer(("localhost", 6789))
# 注册函数
server.register_function(double, "double")
server.register_function(power, "power")
# 服务器一直开启
server.serve_forever()