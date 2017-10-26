# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-10-24 23:09:56
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-24 23:45:29
# @Description: 日志以及异常处理

# 开启DebugLog 打印日志
import urllib.request

httphd = urllib.request.HTTPHandler(debuglevel=1)
httpshd = urllib.request.HTTPSHandler(debuglevel=1)

opener = urllib.request.build_opener(httphd, httpshd)
opener.open('http://edu.51cto.com')

# 控制台会打印出下面的日志

# send: b'GET / HTTP/1.1\r\nAccept-Encoding: identity 
#       User-Agent: Python-urllib/3.5\r\nConnection: close\r\nHost: edu.51cto.com\r\n\r\n'
# reply: 'HTTP/1.1 200 OK\r\n'
# header: Date header: Content-Type header: Transfer-Encoding header: Connection 
# header: Set-Cookie header: Server header: Vary header: Vary header: X-Powered-By 
# header: Set-Cookie header: Set-Cookie header: Set-Cookie header: Load-Balancing 
# header: Load-Balancing [Finished in 1.9s]



# 异常处理
import urllib.error

try:
	urllib.request.urlopen('http://blog.csdn.net', timeout=1)
except urllib.error.HTTPError as e:
	print(e.code, end='')
	print(e.reason, end='')
except urllib.error.URLError as g:
	print(g.reason, end='')

# 上面的异常处理还可以整合一下
try:
	urllib.request.urlopen('http://blog.csdsn.net', timeout=1)
except urllib.error.URLError as e:
	if hasattr(e, 'code'):
		print(e.code, end='')
	if hasattr(e, 'reason'):
		print(e.reason, end='')
