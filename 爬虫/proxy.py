# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-10-24 22:10:17
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-24 22:58:13
# @Description: 设置代理服务器爬取

# 首先补充一下 GET请求和 POST请求的方式
import urllib.request
import urllib.parse

# 1. url 如果有中文的话，使用urllib.request.quote(str)
url1 = r"http://juejin.im/search?query=react"
url2 = r"http://juejin.im/search?query=" + urllib.request.quote('爬虫')

# GET 请求
# data = urllib.request.urlopen(urllib.request.Request(url1)).read()
# with open('./d.html', 'wb') as f:
# 	f.write(data)

# Post请求
# Post请求需要使用 urllib.parse.urlencode(data) 编码一下参数
# 这里一个案例
# param = urllib.parse.urlencode({
# 	'name': '123',
# 	'pass': '123'	
# }).encode('utf-8')

# req = urllib.request.Request(url2, param)
# data = urllib.request.urlopen(req).read()



# 如果爬取一个网页多次，每次都没有换IP，就有可能被服务器屏蔽。
# 所以我们要使用代理，随意在网上找几个代理服务器，记下ip地址和端口
# http://www.xicidaili.com/ 可以在这儿找代理服务器，选用验证时间最短的。
def use_proxy(proxy_addr_list, url):
	if(len(proxy_addr_list)>0):
		try:
			addr = proxy_addr_list.pop()
			proxy = urllib.request.ProxyHandler({'http':addr}) # 设置代理
			opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler) # 注意第二个参数
			data = opener.open(url, timeout=10).read().decode('utf-8')
		except Exception as e:
			print('error', str(e))
			use_proxy(proxy_addr_list, 'http://www.baidu.com')# 递归调用
		else:
			print(len(data))
	else:
		raise IndexError('no member in list')

proxy_addr_list = ['121.31.102.153:8123', '110.73.10.207:8123', '110.73.15.217:8123', '115.200.32.10:8123']

use_proxy(proxy_addr_list, 'http://www.baidu.com')