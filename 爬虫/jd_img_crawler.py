# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-10-28 20:49:11
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-28 21:40:49
# @Description: 爬取京东手机的图片到本地

import urllib.request
import urllib.error
import re

def craw(url, pagenum):
	html = urllib.request.urlopen(url).read()
	html = str(html)

	patter1 = r'<div id="plist".+? <div class="page clearfix">'
	res1 = re.findall(patter1, html)[0]

	patter2 = r'<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">'
	imglist = re.findall(patter2, res1)

	x=1
	for img in imglist:
		imgName = "./imgs/img" + str(pagenum) + str(x) + '.jpg'
		imgUrl = "http://" + img
		try:
			urllib.request.urlretrieve(imgUrl, filename=imgName)
		except urllib.error.URLError as e:
			if hasattr(e, 'code'):
				x+=1
			if hasattr(e, 'reason'):
				x+=1
		x+=1

for i in range(1,2):
	url = "http://list.jd.com/list.html?cat=9987,653,655&page=" + str(i)
	craw(url, i)
