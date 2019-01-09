# author: adam
# 主题：使用TCP（传输控制协议）传输数据流，本脚本作为服务器。
import socket
from datetime import datetime

address = ("localhost", 6789)
max_size = 1000

print("Server start at", datetime.now())
print("Waiting for a client to call.")
# 创建一个套接字
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 将套接字和特定的地址、端口绑定
server.bind(address)
# 开始监听，并最多和5个客户端连接
server.listen(5)

client, addr = server.accept()
data_byte = client.recv(max_size)
data = bytes.decode(data_byte, 'utf-8')

print("At %s %s said: %s"%(datetime.now(), client, data))
client.sendall(b'Are you talking to me?')
client.close()# 与客户端断开连接
server.close()# 关闭服务器