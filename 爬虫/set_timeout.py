# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-10-24 21:05:00
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-24 21:11:28
# @Description: 设置超时时间

import urllib.request

for i in range(1, 100):
    try:
        file = urllib.request.urlopen('http://www.baidu.com', timeout=0.1)
    except Exception as e:
        print('error: {}'.format(str(e)))
    else:
        data = file.read()
        print(len(data))


# 我们爬取百度的网页，超时时间设置为0.1秒，才能看见几个超时的异常。
# 可见百度的服务器是多么的牛逼。
