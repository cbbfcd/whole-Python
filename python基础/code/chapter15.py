# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-09-07 21:02:10
# @Last Modified by:   28906
# @Last Modified time: 2017-09-07 22:04:05


# 服务端
# 客户端 见 client.py
# import socket
# import sys

# # 创建socket对象
# serversocket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # 绑定端口
# host = socket.gethostname()
# port = 8888
# serversocket.bind((host, port))
# # 设置最大链接数，超过排队
# serversocket.listen(5)

# while True:
# 	# 建立客户端连接
# 	clientsocket, addr = serversocket.accept()

# 	print('连接地址{}'.format(addr))

# 	msg = 'welcome'

# 	clientsocket.send(msg.encode('utf-8'))
# 	clientsocket.close()


## 并发服务端
import socketserver

# 我的服务端类，继承BaseRequestHandler
class myServer(socketserver.BaseRequestHandler):

	# 重写handle
	def handle(self):
		while 1:
			# 下面代码等价于conn,addr = socket.accept()
			conn = self.request
			addr = self.client_address
			while 1:
				accept_data = str(conn.recv(1024), encoding='utf-8')
				print(accept_data)
				if accept_data == 'bye':
					break
				send_data = bytes(input("server:"), encoding='utf-8')
				conn.sendall(send_data)
			conn.close()

if __name__ == '__main__':
	server = socketserver.ThreadingTCPServer(('127.0.0.1',8989), myServer)
	server.serve_forever()

