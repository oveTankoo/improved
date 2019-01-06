# author: adam
# 主题：使用Redis来快速搭建一个发布-订阅系统。
# 发布者会发出包含话题和值的消息，订阅者会声明它们对什么感兴趣。
import redis
import random

conn = redis.Redis()
cats = ['siamese', 'persian', 'maine coon', 'norwegian forest']
hats = ['stovepipe', 'bowler', 'tam-o-shanter', 'fedora']

for msg in range(10):
	cat = random.choice(cats)
	hat = random.choice(hats)
	print("Publish:%s wears a %s"%(cat, hat))
	# 每个话题是猫的一个品种，每个消息的值是帽子的一个类型。
	conn.publish(cat, hat)