# author: adam
# 主题：本示例实现一个简单的请求 - 响应对。这是同步的：一个套接字发送请求，另一个发送响应。
# 该文件为发送响应的代码（服务器）。
# 以下为ZeroMQ的套接字类型：1.REQ（同步请求）2.REP（同步响应）3.DEALER（异步请求）4.ROUTER（异步响应）
# 5.PUB（发布）6.SUB（订阅）7.PUSH（扇出）8.PULL（扇入）
import zmq

host = '127.0.0.1'
port = 6789
context = zmq.Context()# 创建一个Context对象：这是一个能保存状态的ZeroMQ对象。
server = context.socket(zmq.REP)# 创建一个REP类型(同步响应)的ZeroMQ套接字。
server.bind("tcp://%s:%s"%(host, port))# 绑定一个套接字，并监听特定地址和端口。

while True:
	# 等待客户端的下一个请求
	request_bytes = server.recv()
	request_str = request_bytes.decode('utf-8')
	print("That voice in my head says:%s"%request_str)

	# 定义响应
	reply_str = "Stop saying: %s"%request_str
	reply_bytes = bytes(reply_str, 'utf-8')
	server.send(reply_bytes)