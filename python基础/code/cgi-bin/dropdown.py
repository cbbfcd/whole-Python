#!D:\python\python.exe
# -*- coding: utf-8 -*-

import cgi, cgitb

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据

if form.getvalue('dropdown'):
	site =  form.getvalue('dropdown')
else:
	site = "没有选择网站"
# 响应页面
print ("Content-type:text/html")
print ()                             # 空行，告诉服务器结束头部
print ('<html>')
print ('<head>')
print ('<meta charset="gbk">')
print ('<title>test</title>')
print ('</head>')
print ('<body>')
print('<h1>下拉选</h1>')
print ('<h3>选择了：{}</h3>'.format(site))
print ('</body>')
print ('</html>')
