# -*- coding: utf-8 -*-
import scrapy
import json
import re
import time
from myspider.items import MyspiderItem


class JuejinSpider(scrapy.Spider):
	name = 'juejin'
	allowed_domains = ['juejin.im', 'timeline-merger-ms.juejin.im']

	start_urls=['http://timeline-merger-ms.juejin.im/v1/get_entry_by_rank?src=web&limit=100&category=all']


	def parse(self, response):
		data = json.loads(response.text,encoding='utf-8')
		entrylist = data['d']['entrylist']
		rankIndex = entrylist[-1]['rankIndex']
		while len(entrylist)>0:
			item = MyspiderItem()
			i = entrylist.pop(0)
			item['title'] = i['title']
			item['originalurl'] = i['originalUrl']
			item['viewscount'] = i['viewsCount']
			item['tags'] = ','.join([t['title'] for t in i['tags']])
			item['collectioncount'] = i['collectionCount']
			item['commentscount'] = i['commentsCount']
			item['categoryname'] = i['category']['name']
			item['categorytitle'] = i['category']['title']
			item['buildtime']= self.handledate2timestamp(i['createdAt'])
			yield item
		else:
			new_link = 'http://timeline-merger-ms.juejin.im/v1/get_entry_by_rank?src=web&limit=100&category=all&before={}'.format(rankIndex)
			yield scrapy.Request(new_link, callback=self.parse)
	
	
	def handledate2timestamp(self, datestr):
		'''处理日期字符串转为时间戳'''
		datestr = datestr[:-1]
		_date = datestr.replace(r'T', ' ')
		milliseconds = _date[-3:]
		timeArray = time.strptime(_date, '%Y-%m-%d %H:%M:%S.%f')
		return str(int(time.mktime(timeArray))) + milliseconds