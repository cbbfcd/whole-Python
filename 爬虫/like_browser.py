# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-11-07 21:38:00
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-11-07 22:17:03
# @Description: 反爬技术之--浏览器伪装

# 前面提到了浏览器伪装技术，但是太简单了。
# 常见的反爬技术有很多，其中之一就是分析用户请求的header。从而判断是不是爬虫
# 所以我们需要让我们的爬虫伪装成浏览器访问。
# 首先看看，请求的header有哪些东西，HTTP的基础知识可以在本项目的根目录下找到。
# 这里简单的再介绍一下，打开Fiddler(一个抓包软件)，然后浏览器访问优酷


# 获取到对应的header如下：
# GET / HTTP/1.1
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0
# Referer: https://www.baidu.com/link?url=b-7IsdZDkmC54HLYSQWK66pQ6j8T7sqZTCcr6LSr2TK&wd=&eqid=ac6479cc0000a335000000055a01b839
# Upgrade-Insecure-Requests: 1
# Connection: keep-alive
# Host: www.youku.com

# Accept表示浏览器支持的数据类型，分别支持html,xhtml,xml,q表示权重，数字越大，优先级越高
# Accept-Language表示浏览器支持的自然语言类型，分别是中文简体、引文，q也是权重
# Accept-Encoding表示支持的内容编码格式，支持gzip压缩、deflate无损压缩
# User-Agent：用户代理，浏览器的信息
# Referer表示来源的网址
# Host表示你请求的网址
# Connection:keep-alive表示持久链接。减少消耗的，HTTP1.1提出



# 实战 -- 我们先不伪装，然后访问网易
# import urllib.request
# import http.cookiejar

# url = 'http://news.163.com/17/1107/10/D2KNV8C900018AOQ.html'
# cjar = http.cookiejar.CookieJar()
# # 设置127.0.0.1代理，这样Fiddler就可以截获
# proxy = urllib.request.ProxyHandler({'http': '127.0.0.1:8888'})
# opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler, urllib.request.HTTPCookieProcessor(cjar))
# data = opener.open(url).read()
# with open('./news.html', 'wb') as f:
# 	f.write(data)

# 通过Fiddler我们捕获了这次请求，观察其header

# Accept-Encoding: identity
# User-Agent: Python-urllib/3.5
# Connection: close
# Host: news.163.com


# 很赤裸裸嘛！

# 我们改进上面的代码，进行伪装
import urllib.request
import http.cookiejar

url = 'http://news.163.com/17/1107/10/D2KNV8C900018AOQ.html'
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Encoding":"utf-8, gb2312",
	"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Referer":"http://www.163.com/",
	"Connection":"keep-alive"
}
cjar = http.cookiejar.CookieJar()
# 设置127.0.0.1代理，这样Fiddler就可以截获
proxy = urllib.request.ProxyHandler({'http': '127.0.0.1:8888'})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler, urllib.request.HTTPCookieProcessor(cjar))
# 加入headers
headerslist = []
for key,value in headers.items():
	item = (key, value)
	headerslist.append(item)

opener.addheaders = headerslist

data = opener.open(url).read()
with open('./news.html', 'wb') as f:
	f.write(data)

# 观察Fiddler中拦截的请求头，看看header基本是与我们设置的一致。 


# 注意：
# 1. "Accept-Encoding":"utf-8, gb2312"； 如果设置成gzip之类的会获取一堆二进制数。因为我们没用浏览器去解析
# 2. "Referer":"http://www.163.com/"；使用Fiddler的时候最后的 / 不要省略。