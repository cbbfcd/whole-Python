# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-11-20 13:38:01
# @Last Modified by:   28906
# @Last Modified time: 2017-11-20 13:40:11
# @Description: 爬取segmentfault网数据

import scrapy

class SegmentFaultSpider(scrapy.Spider):
	name = 'segmentfault'
	allowed_domains = ['']

	start_urls = ['']

	def parse(self, response):
		