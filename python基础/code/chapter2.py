# -*- coding: utf-8 -*-
# @Author: huangteng
# @Date:   2017-08-18 14:32:47
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-08-18 16:00:29
import math
import random
# if

def login(username, pwd):
	if pwd == '123' and username == 'admin':
		print('login success!')
	elif username == 'admin' and pwd != '123':
		print('pwd is error')
	else:
		print('username is not exist')

login('admin', '123') # login success!
login('admin', '1234') # pwd is error
login('adminss', '1234') # username is not exist


# 条件表达式

# color = input('what your favrita color')
# rep = '我也喜欢' if color == 'blue' else '我不是很喜欢哦'
# print(rep)


# break
def testBreak(num):
	for i in range(0, num):
		if i == 2:
			print('i = {} , so bye~'.format(i))
			break
		print('i = {}'.format(i))

testBreak(10)

# continue
def testContinue(num):
	while num < 6:
		pass
		num = num + 1
		if num == 5:
			continue
		print('this num is {}'.format(num))

testContinue(0) # 不会输出this num is 5

# 猜数字 输入-1直接推出
def guess():
	answer = math.floor(100 * (random.random())) # 随机数
	flag = True
	while flag:
		num = int(input('input a number'))
		if num == answer:
			flag = False
			print('恭喜你答对了')
		elif num < answer and num != -1:
			print('小了一点点')
		elif num == -1:
			break
		else:
			print('太大了')
	else:
		print('Bye~~')
guess()