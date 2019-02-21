# 主题：使用 ZeroMQ 发布第 7 章练习 (7) 中的诗（参见 7.3 节），每次发布一个单词。
# 写一个ZeroMQ 客户端来打印出每个以元音开头的单词，再写另一个客户端来打印出所有长度为 5 的单词。忽略标点符号。
# 此处为服务器
import re
import zmq

letter = "We have seen thee, queen of cheese,\
Lying quietly at your ease,\
Gently fanned by evening breeze,\
Thy fair form no flies dare seize.\
All gaily dressed soon you'll go\
To the great Provincial show,\
To be admired by many a beau \
In the city of Toronto.\
Cows numerous as a swarm of bees,\
Or as the leaves upon the trees,"

host = '127.0.0.1'
port = 6789
context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.bind("tcp://%s:%s"%(host, port))
content = [x for x in re.split("[ ,]", letter) if x != '']
for item in content:
	print("I will publish %s"%item)
	item_bytes = item.encode('utf-8')
	pub.send(item_bytes)