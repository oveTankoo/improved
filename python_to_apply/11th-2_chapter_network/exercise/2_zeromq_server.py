# 使用ZeroMQ的REQ与REP类型，来实现简单的请求-响应对
# 
import zmq
from datetime import datetime

host = '127.0.0.1'
port = 6789
context = zmq.Context()
server = context.socket(zmq.REP)	#服务类型为REP-同步响应
server.bind("tcp://%s:%s"%(host, port))
while True:
	# 等待客户端的下一个请求
	print("I'm a server, and waiting for the client to call me.")
	req_bytes = server.recv()
	req_str = req_bytes.decode('utf-8')
	rep_str = bytes(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'utf-8')
	if req_str == 'time':
		server.send(rep_str)
	else:
		handle_bytes = "暗号不对!".encode('utf-8')
		server.send(handle_bytes)