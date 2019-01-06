# author: adam
# 主题：以下是对应的请求代码（客户端），它的类型是REQ（同步请求），调用的是connect()。
# 客户端发送完消息就退出了，但是并没有让服务器退出，所以它一直等待消息。
# 服务器是同步的，一次只能处理一个请求，但是并不会丢弃这段时间达到的其他请求。
# ZeroMQ会在触发某些限制之前一直缓存这些消息，直到他们被处理；这就是 ZeroMQ 中 Q 的意思。
# Q表示队列，M表示消息，Zero表示不需要任何消息发布者。
import time
import zmq

host = '127.0.0.1'
port = 6789

context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect("tcp://%s:%s"%(host, port))

for num in range(1, 6):
	request_str = "message #%s"%num
	request_bytes = request_str.encode('utf-8')
	# 客户端发出请求
	client.send(request_bytes)
	# 客户端接收响应
	reply_bytes = client.recv()
	reply_str = reply_bytes.decode('utf-8')
	# 打印出收到的响应
	print("Sent - %s, received - %s"%(request_str, reply_str))