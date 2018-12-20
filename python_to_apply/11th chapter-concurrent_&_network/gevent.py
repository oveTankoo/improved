from gevent import monkey;monkey.patch_socket()
import gevent
import urllib2

def f(url):
	print("Get: %s"%url)
	resp = urllib2.urlopen(url)
	data = resp.read()
	print("%d bytes received from %s."%(len(data), url))

hosts = ['https://www.python.org', 'https://www.yahoo.com','https://www.github.com']
jobs = [gevent.spawn(f, host) for host in hosts]
gevent.joinall(jobs, timeout = 5)
#for job in jobs:
#	print(job.value)
