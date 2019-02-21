# 练习：当客户端传输请求字符串“time”时，服务器返回当前日期和ISO格式的时间
# author：adam
import socket

address = ('localhost', 6789)
max_size = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'time', address)
data, server = client.recvfrom(max_size)
print("Server said: %s"%data.decode('utf-8'))
client.close()