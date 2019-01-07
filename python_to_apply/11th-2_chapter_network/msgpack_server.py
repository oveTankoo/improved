# author: adam
# 
from msgpackrpc import Server, Address
# Services类把它的方法，暴露为RPC服务
class Services():
	def double(self, num):
		return num * 2

server = Server(Services())
server.listen(Address("localhost", 6789))
server.start()