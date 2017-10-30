# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-10-27 00:01:20
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-27 00:58:11
# @Description: 使用cookie处理会话状态
# 如果不使用cookie的话，访问某网站的另一个页面就会让你再次登陆
import urllib.request
import urllib.parse
import http.cookiejar

# 不使用cookie
url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LZv0O"
param = urllib.parse.urlencode({
	'username': 'weisuen',
	'password': 'aA123456'
}).encode('utf-8')
header = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.50"
# req = urllib.request.Request(url, param)
# req.add_header('User-Agent', header)
# data = urllib.request.urlopen(req).read()
# with open('./no-cookie1.html', 'wb') as f:
# 	f.write(data)

# url2 = 'http://blog.chinaunix.net'
# req2 = urllib.request.Request(url2)
# req2.add_header('User-Agent', header)
# data2 = urllib.request.urlopen(req2).read()
# with open('./no-cookie2.html', 'wb') as g:
# 	g.write(data2)



# 使用cookiejar
req = urllib.request.Request(url, param)
req.add_header('User-Agent', header)
cjar = http.cookiejar.CookieJar()
# cookie处理器
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
# 注册全局的opener
urllib.request.install_opener(opener)
data = opener.open(req).read()
with open('./cookie1.html', 'wb') as f:
	f.write(data)

# 爬另一个页面
url2 = 'http://bbs.chinaunix.net/'
data2 = urllib.request.urlopen(url2).read()
with open('./cookie2.html', 'wb') as g:
	g.write(data2)