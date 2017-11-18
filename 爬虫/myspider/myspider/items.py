# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MyspiderItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	title = scrapy.Field() # 标题
	originalurl = scrapy.Field() # 链接
	viewscount = scrapy.Field() # 浏览次数
	tags = scrapy.Field() # 标签
	collectioncount = scrapy.Field() # 点赞次数
	commentscount = scrapy.Field() # 评论数
	categoryname = scrapy.Field() # 类别名
	categorytitle = scrapy.Field() # 类别标题

	def get_insert_sql(self):
		insert_sql = "insert into arts(title,originalurl,viewscount,tags,collectioncount,commentscount,categoryname,categorytitle) values(%s,%s,%s,%s,%s,%s,%s,%s)"
		params = (self['title'],self['originalurl'],str(self['viewscount']),self['tags'],str(self['collectioncount']),str(self['commentscount']),self['categoryname'],self['categorytitle'])
		return insert_sql,params