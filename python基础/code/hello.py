# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-08-28 14:33:39
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-08-28 14:43:44

'这是一个自定义的模块'    # 模块第一行字符串会被当成是文档

__author__ = 'huangteng'  # __XX__ 表示的是特殊变量

import sys # 引入第三方模块

_someBody = 'guys' # 定义私有变量

def test(): # 自定义函数
	args = sys.argv
	if len(args) == 1:
		print('hello world!')
	elif len(args) == 2:
		print('hello {}!'.format(args[1]))
	else:
		print('hello %s!' % (_someBody))
 # __name__ == '__main__'的作用就是在自己运行是执行，引用的时候不执行。
 # 当在命令行执行python hello.py的时候是会执行的
 # 当被别的模块引入的时候不会执行test()，需要hello.test()才行。
if __name__ == '__main__':
	test()
