# 使用ZeroMQ的REQ与REP类型，来实现简单的请求-响应对
import zmq
from datetime import datetime

host = '127.0.0.1'
port = 6789
context = zmq.Context()
client = context.socket(zmq.REQ)	#服务类型为REQ-同步请求
# 客户端连接指定的套接字
client.connect("tcp://%s:%s"%(host, port))

req_str = 'time'
req_bytes = req_str.encode('utf-8')
client.send(req_bytes)	# 发送请求的内容
# 接收服务器的响应
reply_bytes = client.recv()
reply_str = reply_bytes.decode('utf-8')
print("I sent %s,Received %s."%(req_str, reply_str))
client.close()