# author: adam
import redis

conn = redis.Redis()
# 声明自己感兴趣的话题
topics = ['maine coon', 'persian']
sub = conn.pubsub()
sub.subscribe(topics)

for msg in sub.listen():
	if msg['type'] == 'message':
		cat = msg['channel']
		hat = msg['data']
		print("Subscribe: %s wears a %s"%(cat, hat))