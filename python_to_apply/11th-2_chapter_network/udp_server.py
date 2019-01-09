# author: adam
# 主题：使用UDP（用户数据报协议）进行数据传输，该脚本作为服务器。
# 特点：UDP很快、很轻，不需要建立连接，但是并不可靠。
# UDP发送多个消息，它们可能以任何顺序达到，也有可能全部无法达到）
import socket
from datetime import datetime

server_address = ('localhost', 6789)
max_size = 4096

print("Server start at ",datetime.now())
print("Waiting for a client to call.")
# 服务器创建一个套接字（AF_INET表示要创建一个因特网套接字，SOCK_DGRAM表示要发送和接收数据报-使用UDP）
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 服务器绑定到这个套接字上（监听到达这个IP和端口的所有数据）
server.bind(server_address)

# 接收从绑定的套接字传来的数据报
data, client = server.recvfrom(max_size)
# 打印从客户端发来的数据报
print("At %s %s said %s"%(datetime.now(), client, data))
# 服务器作出回应
server.sendto(b"Are you talking to me?",client)
server.close()# 关闭服务器