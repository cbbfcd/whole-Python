# -*- coding: utf-8 -*-
import scrapy


class Myspd2Spider(scrapy.Spider):
    name = 'myspd2'
    allowed_domains = ['juejin.im']
    start_urls = ['http://juejin.im/']

    def parse(self, response):
        pass
