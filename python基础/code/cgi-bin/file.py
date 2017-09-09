#!D:\python\python.exe
# -*- coding: utf-8 -*-

import cgi, os

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
fileitem = form['file']


if fileitem.filename:
	# 设置文件路径 
	fn = os.path.basename(fileitem.filename)
	open(r'E:\Python\PythonNotes\python基础\files\files.txt', 'wb').write(fileitem.file.read())
	message = '文件 "' + fn + '" 上传成功'
else:
	message = '文件没有上传'
   


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
print ('<h3>{}</h3>'.format(message))
print ('</body>')
print ('</html>')

