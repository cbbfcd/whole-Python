# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-10-28 21:44:34
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-28 23:00:20
# @Description: 爬取csdn上的所有url链接，并去重

import urllib.request
import urllib.error
import re

def getLinks(url):
	header = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52')
	opener = urllib.request.build_opener()
	opener.addheaders = [header]

	data = opener.open(url).read()

	# 获取链接

	pattern = r'(https?:\/\/[\w\-]+(\.[\w\-]+)+([\w\-\.,@?^=%&:\/~\+#]*[\w\-\@?^=%&\/~\+#])?)'
	links = re.findall(pattern, str(data))
	return list(set(links))

url = 'http://www.csdn.net'
links = getLinks(url)
print(len(links))
for i in links:
	print(i[0])