# 练习：当客户端传输请求字符串“time”时，服务器返回当前日期和ISO格式的时间
# author：adam
from datetime import datetime
import socket

address = ('localhost', 6789)
max_size = 4096

print("Waiting for a client to call.")
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(address)

data, client = server.recvfrom(max_size)
now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
data_str = data.decode('utf-8')
reply_bytes = bytes("Current time is %s."%now_str, 'utf-8')
if data_str == 'time':
	server.sendto(reply_bytes, client)
else:
	pass
server.close()