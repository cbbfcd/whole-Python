# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-11-08 21:29:57
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-11-08 22:37:06
# @Description: 定向爬虫


# 定向爬虫 很好理解，就是有目标的去爬取我们需要的数据。
# 要实现一个定向爬虫，需要我们做很多事情：
# 1. 理清楚爬虫的目的
# 2. 设置网址过滤规则，过滤掉不需要的网址，进行URL排序等
# 3. 内容采集规则，只关注我们需要的信息
# 4. 采集任务制定，是采用单线程还是多线程爬虫，或者是多个爬虫
# 5. 对采集的结果进行修正
# 6. 对采集结果进一步的处理，比如存入数据库

# 定向爬虫的核心就是对爬取目标采用的爬取策略和爬取的规则。

# 对于信息的筛选主要的技术是正则匹配、Xpath、xslt等。

# 这里实现一个demo，爬取腾讯视频中对战狼的评论。并且实现自动加载更多
# 通过F12或者Fildder获取其URL。并分析

'''https://coral.qq.com/article/1485880528/comment?commentid=6334021116080339140&reqnum=20
&tag=&callback=jQuery1124021396324269288347_1510148969082&_=1510148969090'''

# 1485880528 -- 视频的ID
# reqnum -- 每次展示20条
# commentid --评论id

# 所以访问地址就是: http://coral.qq.com/article/1485880528/comment?commentid=6334021116080339140&reqnum=20

import urllib.request
import http.cookiejar
import json

# 视频编号
vid = "1485880528"

# 评论起始编号
cid = "6334023219020311359"

# 请求地址
# url = r"http://coral.qq.com/article/{}/comment?commentid={}&reqnum=20".format(vid, cid)

# 伪装成浏览器访问
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
	"Host": "coral.qq.com",
	"Connection": "keep-alive",
	"Referer": "https://v.qq.com/txyp/coralComment_yp_1.0.htm",
	"Accept": "*/*",
	"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Accept-Encoding": "gb2312, utf-8"
}

cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))

headrall = []
for key,value in headers.items():
	headrall.append((key,value))

opener.addheaders = headrall

# # 爬取该网页
# data = opener.open(url).read().decode('utf-8')

# # 构建信息筛选
# obj = json.loads(str(data))['data']
# clist = obj['commentid']

# for item in clist:
# 	print('用户名:{}'.format(item['userinfo']['nick']))
# 	print('评论:{}'.format(item['content']))
# 	print('\n')
        
# 上面就完成了一个评论的爬虫，但是有一个问题就是没有实现加载更多
# 我们改进一下，每次把最后一个数据的id作为参数构造新的url请求


def craw(vid, cid, opener):
	url = r"http://coral.qq.com/article/{}/comment?commentid={}&reqnum=20".format(vid, cid)
	data = opener.open(url).read().decode('utf-8')
	obj = json.loads(str(data))['data']
	clist = obj['commentid']
	return clist

# 爬取前3页的内容：

for page in range(1,4):
	print('--------爬取第{}页内容---------'.format(page))
	data = craw(vid, cid, opener)

	for item in data:
		print('用户名:{}'.format(item['userinfo']['nick']))
		print('评论:{}'.format(item['content']))
		print('\n')

	# 将最后一个commentid作为参数，替换
	cid = data[19]['id']

