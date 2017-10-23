# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-10-23 22:24:30
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-23 22:43:01
# @Description: urllib的基础用法

import urllib.request

file = urllib.request.urlopen('http://www.baidu.com')

with open('./baidu.html', 'wb') as f:
	# file.read() 表示读取所有的数据
	# file.readline() 表示读取一行
	# file.readlines() 表示读取所有行的数据，返回一个列表
	
	#f.write(file.read())
	for i in file.readlines():
		f.write(i)

# 可以使用urllib.request.urlretrieve(url, filename='')
urllib.request.urlretrieve('http://edu.51cto.com', filename='./cto.html')
# 清楚缓存
urllib.request.urlcleanup()


# 爬取的file可以获取其信息
print(file.info()) # Content-Type: text/html Content-Length: 6406
print(file.getcode()) # 200
print(file.geturl()) # http://www.baidu.com

# 对url进行编码和解码
print(urllib.request.quote('http://www.sina.com.cn')) # http%3A//www.sina.com.cn
print(urllib.request.unquote('http%3A//www.sina.com.cn')) # http://www.sina.com.cn

