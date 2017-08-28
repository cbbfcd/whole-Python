# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-08-28 13:46:35
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-08-28 14:47:10

# 模块

import sys
print(sys.path)
print(dir(sys))

# 引入模块测试
import hello
hello.test() # hello world!
print(hello.__name__,hello.__author__) # hello huangteng
