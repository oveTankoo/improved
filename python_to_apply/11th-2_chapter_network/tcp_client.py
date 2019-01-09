# author: adam
# 主题：使用TCP（传输控制协议）传输数据流，本脚本作为客户端。
import socket
from datetime import datetime

address = ("localhost", 6789)
max_size = 1000

print("The client start at", datetime.now())
# 创建一个套接字
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 与服务器建立连接
client.connect(address)

client.sendall(b'Hey')
# 接收响应
data_byte = client.recv(max_size)
data = bytes.decode(data_byte, 'utf-8')
# 打印响应
print("At %s someone replied: %s."%(datetime.now(), data))
client.close()