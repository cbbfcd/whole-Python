# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-10-30 22:10:32
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-11-01 10:36:57
# @Description: 搜狗微信爬虫
import time
import urllib.request
import urllib.error
import urllib.parse
import re


def getLinksByProxy(proxys, url):
    '''不同的代理来爬链接，避免被禁了'''
    if (len(proxys) > 0):
        try:
            proxy = proxys.pop()
            _proxy = urllib.request.ProxyHandler({'http': proxy})
            opener = urllib.request.build_opener(
                _proxy, urllib.request.HTTPHandler)
            opener.addheaders = [
                ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52')]
            data = opener.open(url).read().decode('utf-8')
            links = re.findall(
                r'<div class="txt-box">.*?(http://.*?)".*?</em>(.*?)</a>', str(data), re.S)
            # 访问次数过多就会要求输入验证码
            if not len(links):
                print('打印验证码')
                checkCode = re.findall(
                    r'<img id="seccodeImage".*?src="(.*?)".*?>', str(data), re.S)
                checkCodeUrl = 'http://weixin.sogou.com/antispider/' + \
                    checkCode[0]
                imgData = urllib.request.urlopen(checkCodeUrl).read()
                with open('./check.png', 'wb') as f:
                    f.write(imgData)
        except Exception as e:
            print('error', str(e))
            time.sleep(60)
            getLinksByProxy(proxys, url)
        else:
            return links
    else:
        print('list is empty')


def outHtml(data):
    '''打印出爬取的结果'''
    print(data)
    if not data:
        print('获取数据为空')
        return
    with open('./weixin.html', 'w') as f:
        pageheader = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Document</title>
            </head>
            <body>
        '''
        content = ''
        for i in data:
            content = '<a href=' + \
                (i[0]).replace('amp;', '') + '>' + i[1] + '</a>'
        pagebody = '<div><ul>' + content + '</ul></div></body></html>'
        html = pageheader + pagebody
        f.write(html)


proxys = ['27.219.198.237:8118', '42.242.189.239:4336', '113.116.144.164:9000', '60.169.78.218:808',
          '110.16.80.106:8080', '175.17.1.143:8080', '113.65.189.191 :9797']
key = urllib.request.quote('前端')
url = 'http://weixin.sogou.com/weixin?query={}&type={}&page={}'.format(
    key, '2', '1')
outHtml(getLinksByProxy(proxys, url))
