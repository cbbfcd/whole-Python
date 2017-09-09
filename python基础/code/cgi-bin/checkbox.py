#!D:\python\python.exe
# -*- coding: utf-8 -*-

import cgi, cgitb

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据

if form.getvalue('Google'):
	google = "yes"
else:
	google = "no"
if form.getvalue('FaceBook'):
	facebook = "yes"
else:
	facebook = "no"
# 响应页面
print ("Content-type:text/html")
print ()                             # 空行，告诉服务器结束头部
print ('<html>')
print ('<head>')
print ('<meta charset="gbk">')
print ('<title>test</title>')
print ('</head>')
print ('<body>')
print('<h1>checkbox测试</h1>')
print ('<h3>选择了google吗？：{}</h3>'.format(google))
print ('<h3>选择了facebook吗？：{}</h3>'.format(facebook))
print ('</body>')
print ('</html>')
