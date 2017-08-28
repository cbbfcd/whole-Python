# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-08-28 09:40:13
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-08-28 10:59:53
import collections
import sys

# 迭代
str = iter(['a', 'b', 'c'])
print(next(str), end=' ') # a
print(next(str), end=' ') # b


str2 = iter('abc')
print(next(str2)) # a

# 判断是否可以迭代

print( isinstance('abc', collections.Iterable) ) # True

# 循环迭代
ls = '1234'
it = iter(ls)
# for i in it:
# 	print(i, end=',') # 1,2,3,4,

# while True:
# 	try:
# 		print(next(it))
# 	except StopIteration as e:
# 		sys.exit()
	
# 遍历索引

lis = ['aa', 'bb', 'cc']
for i,t in enumerate(lis):
	print('索引：{}，值：{}'.format(i,t))



# 生成器

# 1. 快捷创建

# 回忆创建列表的快捷语法
list1 = [ n*n for n in range(10) if n % 2 ==0 ]
print(list1) # [0, 4, 16, 36, 64]

# 创建生成器
gener1 = ( n*n for n in range(10) if n % 2 ==0 )
print(gener1) # <generator object <genexpr> at 0x0000028CD6046830>
print(next(gener1)) # 0
print(next(gener1)) # 4
print(next(gener1)) # 16

# 一直next()下去太麻烦，还是循环吧
for i in gener1:
	print(i, end=' ') # 36 64


# 斐波拉契
def _fibonacci(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a+b
		n += 1 
	return 'done'
_fibonacci(6)

# 斐波拉契生成器
def _gener_fibonacci(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b
		n += 1 
	return 'done'

# 生成器函数返回一个生成器对象，它是一个iterator
g = _gener_fibonacci(6)
print( isinstance(g, collections.Iterator) ) # True
# for 循环打印不出return的语句'done'
# for i in g:
# 	print(i) # 1 1 2 3 5 8

# 想要输出迭代完了return的'done'需要捕获StopIteration异常。
def print_g(x):
	while True:
		try:
			print(next(x), end=' ')
		except StopIteration as e: 
			print(e.value)
			break
print_g(g) # 1 1 2 3 5 8 done