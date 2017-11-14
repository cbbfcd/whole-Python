# -*- coding: utf-8 -*-
# 最简单的一个爬虫 demo
import scrapy
from myspider.items import MyspiderItem


class JuejinSpider(scrapy.Spider):
    name = 'juejin'
    allowed_domains = ['juejin.im']
    start_urls = ['http://juejin.im/']

    def parse(self, response):
        item = MyspiderItem()
        item['title'] = response.xpath('/html/head/title/text()').extract()
        print(item['title'][0])
