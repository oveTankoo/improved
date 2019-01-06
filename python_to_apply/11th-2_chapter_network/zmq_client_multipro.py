# author: adam
# 主题：以下是使用多进程（Pool）发送请求的代码（客户端），它的类型是REQ（同步请求），调用的是connect()。
import time
import zmq
from multiprocessing import Pool

host = '127.0.0.1'
port = 6789

context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect("tcp://%s:%s"%(host, port))

start = time.time()

def client_behave(num):
	request_str = "message #%s"%num
	request_bytes = request_str.encode('utf-8')
	# 客户端发出请求
	client.send(request_bytes)
	# 客户端接收响应
	reply_bytes = client.recv()
	reply_str = reply_bytes.decode('utf-8')
	# 打印出收到的响应
	print("Sent - %s, received - %s"%(request_str, reply_str))

if __name__ == '__main__':
	p = Pool(4)
	for i in range(1,6):
		p.apply_async(client_behave, args = (i,))
	p.close()
	p.join()
	end = time.time()
	print("Process has wasted: %0.6fs."%(end - start))