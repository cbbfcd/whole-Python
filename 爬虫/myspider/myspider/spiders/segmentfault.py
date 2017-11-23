# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-11-20 13:38:01
# @Last Modified by:   28906
# @Last Modified time: 2017-11-23 12:20:18
# @Description: 爬取segmentfault网数据

import scrapy
from myspider.items import MyspiderItem
import re


class SegmentFaultSpider(scrapy.Spider):
    name = 'segmentfault'
    allowed_domains = ['segmentfault.com']
    start_urls = ['http://segmentfault.com/news']

    def parse(self, response):
        # 点赞数
        collectioncounts = response.xpath('//span[@class="stream__item-zan-number"]/text()').extract()
        # 评论数
        commentscounts = response.xpath('//span[@class="news__item-comment-box"]/text()').extract()
        # title
        titles = response.xpath('//h4[@class="news__item-title"]/a/text()').extract()
        # link
        originalurls = response.xpath('//h4[@class="news__item-title"]/a/@href').extract()
        # categoryname
        categorynames = response.xpath('//a[@class="ml10 "]/text()').extract()
        # categorytitle
        categorytitles = response.xpath('//a[@class="ml10 "]/@href').extract()
        # 当前是第几页
        page = int(response.xpath('//ul[@class="pagination"]/li[@class="active"]/a/text()').extract()[0])

        items = []
        for i in range(0, len(collectioncounts)):
            item = MyspiderItem()
            item['title'] = titles[i]
            item['commentscount'] = commentscounts[i]
            item['collectioncount'] = collectioncounts[i]
            item['originalurl'] = 'http://segmentfault.com' + originalurls[i]
            item['categoryname'] = categorynames[i]
            item['categorytitle'] = re.sub(r'\/(\w+)\/(\w+)', r'\2', categorytitles[i])
            items.append(item)

        for index,item in enumerate(items):
            yield scrapy.Request(item['originalurl'], callback=self.getviewscount, meta={'item': item,'page':page, 'index':index})
        
        new_link = 'http://segmentfault.com/news?page={}'.format(str(page+1))
        yield scrapy.Request(new_link, self.parse)

    def getviewscount(self, res):
        item = res.meta['item']
        page = res.meta['page']
        index = res.meta['index']
        item['viewscount'] = res.xpath('//strong[@class="no-stress"]/text()').extract()[0] if re.search(r'shareId', item['originalurl']) == None else 0
        taglist = res.xpath('/html/body/div[3]/div[2]/div/div/div/div[1]/div/div/ul/*/a/text()').extract() if re.search(r'shareId', item['originalurl']) == None else ''
        item['tags'] = ",".join(taglist) if len(taglist)>0 else 'no-tags'
        print('.....................爬取第{}页，第{}条数据..................'.format(str(page), str(index+1)))
        yield item
