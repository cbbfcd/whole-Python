# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-11-02 21:55:12
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-11-02 23:41:06
# @Description: 多线程爬虫

import urllib.request
import urllib.error
import re
import threading
import queue
import time
import sys
import json

urlqueue = queue.Queue()


class getFrontend(threading.Thread):
    '''获取掘金/前端数据'''

    def __init__(self, url, urlqueue):
        self.url = url
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue

    def run(self):
        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52')]
        req = urllib.request.Request(self.url)
        data = urllib.request.urlopen(req).read().decode('utf-8')
        #data = opener.open(self.url).read().decode('utf-8')
        dictstr = json.loads(str(data))['d']
        urllist = dictstr['entrylist']
        # pattern = r'<div class="info-row title-row" data-v-d13ddee8><!----><!----><a href="(.*?)" target="_blank" rel="" st:name="title" class="title" data-v-d13ddee8>(.*?)</a>'
        # urllist = re.findall(pattern, str(data), re.S)
        if(len(urllist)):
            for i in range(0, len(urllist)):
                print('线程1开始放进第{}条数据进队列'.format(i))
                self.urlqueue.put(urllist[i])


class makeHtml(threading.Thread):
    '''起一个线程写数据到页面'''

    def __init__(self, urlqueue):
        self.urlqueue = urlqueue
        threading.Thread.__init__(self)

    def run(self):
        page = '<!DOCTYPE html><head><meta charset="UTF-8"><title>juejin</title></head><html lang="en"><body><div><ul>'
        with open('./juejin.html', 'wb') as f:
            f.write(page.encode('utf-8'))
        while(True):
            print('线程2开始写页面')
            item = self.urlqueue.get()
            content = '<li><a href="{}">{}</a></li>'.format(item['originalUrl'], item['title'])
            with open('./juejin.html', 'ab') as f:
                f.write(content.encode('utf-8'))
            if(self.urlqueue.empty()):
                break
        with open('./juejin.html', 'ab') as f:
            f.write('</ul></div></body></html>'.encode('utf-8'))

t1 = getFrontend('http://timeline-merger-ms.juejin.im/v1/get_entry_by_rank?src=web&limit=150&category=5562b415e4b00c57d9b94ac8', urlqueue)
t1.start()

t2 = makeHtml(urlqueue)
t2.start()
