# -*- coding: utf-8 -*-
import scrapy


class Myspd3Spider(scrapy.Spider):
    name = 'myspd3'
    allowed_domains = ['juejin.im']
    start_urls = ['http://juejin.im/']

    def parse(self, response):
        pass
