# -*- coding: utf-8 -*-
import scrapy


class Myspd1Spider(scrapy.Spider):
    name = 'myspd1'
    allowed_domains = ['juejin.im']
    start_urls = ['http://juejin.im/']

    def parse(self, response):
        pass
