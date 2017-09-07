# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-09-07 21:58:16
# @Last Modified by:   28906
# @Last Modified time: 2017-09-07 21:58:32
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
	print(''.join(("client2接受内容:", accept_data)))
s.close()