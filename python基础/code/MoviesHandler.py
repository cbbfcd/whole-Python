# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-09-03 19:49:56
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-03 21:08:18
# @description: 解析Movies.xml的handler

import xml.sax

# 解析movies.xml的handler类，必须继承ContentHandler
# 通俗的理解 执行顺序是 startDocument->startElement->characters->endElement->endDocument

class MoviesHandler(xml.sax.ContentHandler):
	
	_movies = []

	item = {

	}

	def __init__(self):
		self.CurrentData = ""
		self.type = ""
		self.format = ""
		self.year = ""
		self.rating = ""
		self.stars = ""
		self.description = ""

	# 文档开始
	def startDocument(self):
		print('开始解析...')

	# 遇到element时调用
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag == 'movie':
			title = attributes['title']
			self.item['title'] = title


	# 标签结束的时候调用
	def endElement(self, tag):
		if self.CurrentData == 'type':
			self.item['type'] = self.type

		if self.CurrentData == 'format':
			self.item['format'] = self.format

		if self.CurrentData == 'year':
			self.item['year'] = self.year

		if self.CurrentData == 'rating':
			self.item['rating'] = self.rating

		if self.CurrentData == 'stars':
			self.item['stars'] = self.stars

		if self.CurrentData == 'description':
			self.item['description'] = self.description

		if tag == 'movie':
			self._movies.append(self.item)
		
		self.CurrentData = ""

	# 读取内容
	def characters(self, content):
		if self.CurrentData == 'type':
			self.type = content

		if self.CurrentData == 'format':
			self.format = content

		if self.CurrentData == 'year':
			self.year = content

		if self.CurrentData == 'rating':
			self.rating = content

		if self.CurrentData == 'stars':
			self.stars = content

		if self.CurrentData == 'description':
			self.description = content

	# 结束
	def endDocument(self):
		print('over....')
		print(self._movies)

if __name__ == '__main__':
	
	# 创建parser
	parser = xml.sax.make_parser()

	# turn off namepsaces
	parser.setFeature( xml.sax.handler.feature_namespaces, 0 )

	# 重写ContentHandler
	movieHandler = MoviesHandler()

	parser.setContentHandler( movieHandler )

	parser.parse(r'../files/movies.xml')