# author: adam
# 客户端身份，通过地址&端口和服务器连接，使用RPC服务调用已注册的函数。
import xmlrpc.client

# 连接服务器
proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
num = 10
# 使用RPC调用已注册的函数
result_1 = proxy.double(num)
result_2 = proxy.power(num)
# 打印返回值
print("Double %s is %s.Pow %s is %s."%(num, result_1, num, result_2))