#!D:\python\python.exe
# -*- coding: utf-8 -*-

import cgi, cgitb


# 响应页面
print ("Content-type:text/html")
print("Set-Cookie: name='test';expires=Wed, 28 Aug 2016 18:30:00 GMT")
print ()                             # 空行，告诉服务器结束头部
print ('<html>')
print ('<head>')
print ('<meta charset="gbk">')
print ('<title>test</title>')
print ('</head>')
print ('<body>')
print('<h1>设置cookie</h1>')
print ('</body>')
print ('</html>')
