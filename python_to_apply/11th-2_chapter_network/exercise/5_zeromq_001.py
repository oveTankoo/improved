# 主题：使用 ZeroMQ 发布第 7 章练习 (7) 中的诗（参见 7.3 节），每次发布一个单词。
# 写一个ZeroMQ 客户端来打印出每个以元音开头的单词，再写另一个客户端来打印出所有长度为 5 的单词。忽略标点符号。
# 此处为一个订阅每个以元音开头的单词的ZeroMQ 客户端
import re
import zmq

host = '127.0.0.1'
port = 6789
context = zmq.Context()
sub = context.socket(zmq.SUB)
sub.connect("tcp://%s:%s"%(host, port))

topics = ''
# 声明感兴趣的话题
#for topic in topics:
sub.setsockopt(zmq.SUBSCRIBE, topics.encode('utf-8'))
while True:
	recv_bytes = sub.recv()
	print(recv_bytes)
	recv_str = re.match("[aeiou]", recv_bytes.decode("utf-8"))
	if recv_str:
		print("Subscribe: %s"%recv_str.group())
	else:
		pass