# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-08-24 09:19:03
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-12 10:14:37
import math
import functools

# 函数示例

def _area(r):
	'''
	根据传入的半径计算圆的面积；
	比如:
	>>> area(1)
	3.1415926...
	'''
	return math.pi*r**2

print(_area(5)) # 78.53981633974483
print(_area.__doc__) # 根据传入的半径计算圆的面积；
					#比如:
					#>>> area(1)
					#3.1415926...

# 变量的作用域

name = 'James Kyle'

def _changeName(new_name):
	'''
	改变名称的方法；
	比如： _changeName('james')
	'''
	# global name # 加了全局变量声明之后，会输出hello, tom;这里的name就是外面的全局变量name了
	            # 不然就会被当成是一个与外层全局变量无关的局部变量name。
	name = new_name

def _sayHello():
	'''
	sayhello的function；
	比如： _sayHello('james')
	输出: hello james
	'''
	print('hello, {}'.format(name))

_sayHello() # hello, James Kyle
_changeName('tom')
_sayHello() # hello, James Kyle


# 参数传递
num = 5
def set1(x):
	"""
	设置值为1的方法
	"""
	x = 1
set1(num)
print(num) # 5

list1 = [1, 2, 3]
def updateList(l):
	l[0] = 'test'

updateList(list1)
print(list1) # ['test', 2, 3]

# 关键字参数
def _someWords(age, name, job):
	'''
	打印一句话的函数
	'''
	print("i'm {} and i'm a {} who age is {} ".format(name, job, age))
	return;

_someWords(age=25, name='jack', job='student') # i'm jack and i'm a student who age is 25
_someWords(name='tom', age=18, job='coolboy') # i'm tom and i'm a coolboy who age is 18

# 默认参数
def _someInfo(name, age, job='student'):
	'''
	打印一句话的函数
	'''
	print("i'm {} and i'm a {} who age is {} ".format(name, job, age))
	return;

_someInfo('tom',age=18) # i'm tom and i'm a student who age is 18 


# 踩坑
def test_m(L = []):
	L.append('END')
	print(L)
test_m() # ['END']
# 再调用
test_m() # ['END', 'END']


# 不定长参数
def getArr( num ,*arr ):
	'''
	打印参数
	'''
	print(num)
	for i in arr:
		print('输出:',i, end=' ')

	return;

getArr(5) # 5
getArr(10,20,30,40) #  10 输出: 20 输出: 30 输出: 40

# 匿名函数

global_num = 1000
myFunc = lambda x: x+global_num
print(myFunc(1)) # 1001

# 配合全局函数 filter, map, reduce使用
test_list = [0,1,2,3,4,5,6,7,8,9]
new_list1 = filter( lambda i: i%2 == 0, test_list )
print(list(new_list1)) # [0, 2, 4, 6, 8]

# 但是lambda在这里个人感觉还不如 for...in...if清晰好用
print([x for x in test_list if x % 2 == 0]) # [0, 2, 4, 6, 8]

# map
new_list2 = map( lambda x: x * 2 + 10, test_list )
print(list(new_list2)) #[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
print([x*2+10 for x in test_list]) #[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

# reduce
# python3中从全局移除了reduce,放进了functools中。
val = functools.reduce( lambda x, y: x+y, test_list)
print(val) # 45


# 作用域示例
_x = int(5) # 内建作用域
_y = 5 # 全局作用域
def _test1():
	_z = 5 # 局部外局部作用域
	def _test2():
		_d = 5 # 局部作用域

# 访问if内的变量
if(1):
	_test3 = 5

print(_test3) #5

# 修改非外层全局作用域

def __test():
	__num = 5
	def __change():
		nonlocal __num
		__num = 6
		print('inner: ',__num, end=' ,outer ')
	__change()
	return __num

print(__test()) # inner:  6 ,outer 5

# 补充说明 不定长参数 **的使用
def _dictTest(a, b, **c):
	print(a, b, c)

print(_dictTest('china', 'sichuan', city='chengdu', area='jinjiang'))
#china sichuan {'area': 'jinjiang', 'city': 'chengdu'}
#print(_dictTest('china', 'sichuan', 'chengdu', 'jinjiang')) # 报错

__num1 = 1000
def __test3():
	#global __num1
	__num1 = 1001
	print('this is jbw {}'.format(__num1), end=" ")
	def __test4():
		nonlocal __num1
		__num1 = 1002
	__test4()
	return __num1

print(__test3()) 


# 常见的错误
a = 10
def __error():

	'''
	常见错误函数
	'''
	#a += 1 # 局部变量“a”在赋值前被引用
	print(a) 

__error()



# 递归函数和尾递归优化

def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n-1)

print(fact(5)) # 120


# 尾递归优化
def fact2(n):
	return fact_iter(n, 1)

def fact_iter(num, p):
	if num == 1:
		return p
	return fact_iter(num-1, num*p)

print(fact2(5)) #120