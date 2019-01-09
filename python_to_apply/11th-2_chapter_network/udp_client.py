# author: adam
# 主题：使用UDP（用户数据报协议）进行数据传输，该脚本作为客户端。
# 客户端需要知道服务器的地址和端口，但是并不需要指定自己的端口。它的端口是由系统自动分配。
import socket
from datetime import datetime

server_address = ("localhost", 6789)
max_size = 4096

print("The client Start at", datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 向套接字上传送数据报
client.sendto(b'Hey', server_address)
# 接收服务器传回的响应
data, server = client.recvfrom(max_size)
# 打印响应并关闭客户端
print("At %s %s reply %s"%(datetime.now(), server, data))
client.close()