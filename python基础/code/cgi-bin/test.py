#!D:\python\python.exe
# -*- coding: utf-8 -*-

import cgi
import cgitb


# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
user = form.getvalue('username')
pwd = form.getvalue('password')

# 响应页面
print ("Content-type:text/html")
print ()                             # 空行，告诉服务器结束头部
print ('<html>')
print ('<head>')
print ('<meta charset="gbk">')
print ('<title>test</title>')
print ('</head>')
print ('<body>')
print ('<h2>用户名：{}</h2>'.format(user))
print ('</body>')
print ('</html>')

