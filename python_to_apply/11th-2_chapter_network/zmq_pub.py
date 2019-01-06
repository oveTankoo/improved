# 主题：利用ZeroMQ的PUB和SUB套接字，来重写猫-帽子示例
# 由于ZeroMQ没有核心服务器，因此每个发布者都会发送给所有订阅者。
# 发布者发送完消息，就会退出。
import time, random
import zmq

host = '*'
port = 6789
ctx = zmq.Context()
pub = ctx.socket(zmq.PUB)

pub.bind("tcp://%s:%s"%(host, port))

cats = ['siamese', 'persian', 'maine coon', 'norwegian forest']
hats = ['stovepipe', 'bowler', 'tam-o-shanter', 'fedora']
time.sleep(1)

for msg in range(10):
	cat = random.choice(cats)
	cat_bytes = cat.encode("utf-8")#猫用utf-8格式编码
	hat = random.choice(hats)
	hat_bytes = hat.encode("utf-8")#帽子用utf-8格式编码
	print("Publish: %s wears a %s."%(cat, hat))
	pub.send_multipart([cat_bytes, hat_bytes])