# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-10-23 22:44:36
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-23 23:19:20
# @Description: 设置header伪装成浏览器访问


# 部分网站有反爬虫设置
# 我们可以伪装成浏览器去访问，方法就是设置 User-Agent



# 比如我们去爬取掘金上的博客
import urllib.request

file = urllib.request.urlopen('https://juejin.im/post/59edb21251882546d71e8232')
print(file.getcode()) # 纳尼  竟然没有报403 Forbidden

# 将就吧，就是假如出现403的错误，我们可以伪装成浏览器去访问。
# 首先获取User-Agent,这一步通过随便打开一个百度，F12，然后去找，我就不细说了
user_agent_str = r"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.50 Name"

# 2种方式添加header

# 1. build_opener()
# headers = ('User-Agent',user_agent_str)
# opener = urllib.request.build_opener()
# opener.addheaders = [headers]
# data = opener.open('https://juejin.im/post/59edb21251882546d71e8232').read()
# print(data)


# 2. add_header()
req = urllib.request.Request('https://juejin.im/post/59edb21251882546d71e8232')
req.add_header("User-Agent", user_agent_str)
data = urllib.request.urlopen(req).read()
with open('./b.html', 'wb') as f:
	f.write(data)