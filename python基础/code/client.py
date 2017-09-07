# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-09-07 21:19:30
# @Last Modified by:   28906
# @Last Modified time: 2017-09-07 21:56:51


# import socket
# import sys

# # 创建 socket 对象
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# # 获取本地主机名
# host = socket.gethostname() 

# # 设置端口好
# port = 8888

# # 连接服务，指定主机和端口
# s.connect((host, port))

# # 接收小于 1024 字节的数据
# msg = s.recv(1024)

# s.close()

# print (msg.decode('utf-8'))



## 并发客户端 client1
import socket

s = socket.socket()
s.connect(('127.0.0.1', 8989))

while True:
	msg = input('client:')
	send_data = bytes(msg, encoding='utf-8')
	s.sendall(send_data)
	if msg == 'bye':
		break
	accept_data = str(s.recv(1024), encoding='utf-8')
	print(''.join(("接受内容:", accept_data)))
s.close()