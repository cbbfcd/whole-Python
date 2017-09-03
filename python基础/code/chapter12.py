# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-09-03 19:01:00
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-03 21:36:32


# JSON
import json

# python字典编码为 json数据
dic = {
	'name' : 'tom',
	'age' : 25
}

json_str = json.dumps(dic)
print('原始数据:{}'.format(repr(dic))) # 原始数据:{'age': 25, 'name': 'tom'}
print('json数据:{}'.format(json_str)) # json数据:{"age": 25, "name": "tom"}

# json 对象转为 Python字典
new_dic = json.loads(json_str)
print(new_dic['name']) # tom



# 读取json文件
# 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据
with open(r'../files/jt.json', 'r', encoding='utf-8') as f:
	data = json.load(f)
	print(data) # {'name': 'Python3基础', 'version': '1.0.0', 'author': 'taylor huang'}

data1 = {
	"time" : "2017-9-3"
}
# 写入json数据
with open(r'../files/jt.json', 'w', encoding='utf-8') as ff:
	json.dump(data1, ff)




# xml
# 1. sax解析xml
# 该方式适用于大型项目中，基于事件驱动，最重要的就是写一个ContentHanlder类实现自己的业务需求
# 步骤:
#      1. 创建一个新的解析器对象并返回 利用sax.xml.make_parser([parser_list])
#      2. 然后解析 xml.sax.parse( xmlfile, contenthandler[, errorhandler])
#         还可以解析xml字符串  xml.sax.parseString(xmlstring, contenthandler[, errorhandler])

# demo
# ContentHandler实现见 MoviesHandler.py


# 2. dom解析xml
# python中用xml.dom.minidom来解析xml文件

import xml.dom.minidom

_movies = {}
_movies_list = []

# 使用minidom解析器打开 XML 文档
DOMTree =  xml.dom.minidom.parse(r'../files/movies.xml')

# 获取根元素
collection = DOMTree.documentElement
# 获取根元素的属性
if collection.hasAttribute('shelf'):
	_movies['shelf'] = collection.getAttribute('shelf')

# 获取所有元素
movies = collection.getElementsByTagName('movie')

# 遍历解析
for m in movies:
	_movies_item = {}
	if m.hasAttribute('title'):
		_movies_item['title'] = m.getAttribute('title')

	types = m.getElementsByTagName('type')[0]
	_movies_item['type'] = types.childNodes[0].data

	formats = m.getElementsByTagName('format')[0]
	_movies_item['format'] = formats.childNodes[0].data

	years = m.getElementsByTagName('year')[0]
	_movies_item['year'] = years.childNodes[0].data

	rating  = m.getElementsByTagName('rating')[0]
	_movies_item['rating '] = rating .childNodes[0].data

	stars = m.getElementsByTagName('stars')[0]
	_movies_item['stars'] = stars.childNodes[0].data

	description = m.getElementsByTagName('description')[0]
	_movies_item['description'] = description.childNodes[0].data

	_movies_list.append(_movies_item)

print(_movies_list)