"""主题：订阅者向特定地址和端口上的套接字发送感兴趣的话题，然后收到发布者散布的消息
订阅者开启后不会自动退出，就向雷达一直扫描，匹配声明的话题就获取。"""
import zmq

HOST = '127.0.0.1'
PORT = 6789

CTX = zmq.Context()	#create a zmq Context。
# Create a Socket associated with this Context。socket(self, socket_type, **kwargs))
sub = CTX.socket(zmq.SUB)
sub.connect("tcp://%s:%s"%(HOST, PORT))	#Connect to a remote 0MQ socket。connect(addr)
# 感兴趣的话题
TOPICS = ['maine coon', 'persian']

for topic in TOPICS:
	# Set socket options。
	sub.setsockopt(zmq.SUBSCRIBE, topic.encode("utf-8"))
while True:
	# 调用recv_multipart()，可以收到消息的多个部分，并使用第一部分判断话题是否匹配。
	cat_bytes, hat_bytes = sub.recv_multipart()
	cat = cat_bytes.decode("utf-8")
	hat = hat_bytes.decode("utf-8")
	print("Subscribe: %s wears a %s."%(cat, hat))