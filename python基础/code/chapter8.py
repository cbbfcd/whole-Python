# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-08-29 21:57:22
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-17 00:19:33

# 语法
class Person():
	pass


# 一个简单的实例
class myClass():
	"""
	一个简单的实例
	"""
	name = 'tom'
	def sayHello(self):
		return 'hello world'

a = myClass()
print('成员变量: {}'.format(a.name)) # 成员变量: tom
print('方法输出: {}'.format(a.sayHello())) # 方法输出: hello world

# 构造方法
class newClass():

	'''
	含构造方法的类
	'''

	def __init__(self, message, name):
		self.m = message
		self.x = name

b = newClass('message','tom')
print('输出：{},{}'.format(b.m, b.x)) # 输出：message,tom

# 私有变量
class Players():
	_name = 'Tom'
	__job = 'basketball player'

c = Players()
# 我们约定可以使用_name表示私有变量，但是，这只是约定。并不代表不可以访问。
# 如果我们用__job表示，python会认为它就是私有的，不能直接访问的，需要使用 ._类名__job访问。
print('name:{}'.format(c._name)) # name:Tom
print('job:{}'.format(c._Players__job)) # job:basketball player

# 继承

class Animals():

	def __init__(self, name):
		self.name = name

	def run(self):
		return '{} is running'.format(self.name)

class Cat(Animals):

	def __init__(self, name):
		self.name = name


cat = Cat('jack')
print('name is {}, and {}'.format(cat.name, cat.run())) # name is jack, and jack is running


# 多继承

class A():
	'''
	只是演示多继承，省略构造器了
	'''
	def speaker(self):
		return 'it from A'

class B():
	'''
	只是演示多继承，省略构造器了
	'''
	def speaker(self):
		return 'it from B'

class C(B, A):
	pass

print(C().speaker()) # it from B

# 装饰器

def cal(type):
	'''
	根据类型进行不同的计算
	'''
	def cal_sometype(func):
		def wrapper(*args, **kw): # (*args, **kw) 表示任意参数
			if type == 'average':
				print('这是求平均数', end=' ')
			elif type == 'sum':
				print('这是求和操作', end=' ')

			return func(*args, **kw)
		return wrapper
	return cal_sometype

@cal(type='sum')
def sum1(*args):
	return sum(args)

print(sum1(2,5,8)) # 这是求和操作 15


@cal(type='average')
def aver(*args):
	return sum(args)/len(args)
print(aver(2,5,8)) # 这是求平均数 5.0


# __slots__
class D():
	__slots__ = ('name', 'age')

d = D()
d.name = 'jack'
d.age = 25
#d.job = 'student' # 这个会报错，只能操作__slots__定义的那些属性


# @property
class Student():

	@property
	def score(self): # 相当于getter
		return self._score

	@score.setter
	def score(self, value): # 相当于setter
		if not isinstance(value, int):
			raise ValueError('score must be a number')
		if value < 0 or value > 150:
			raise ValueError('score must be 0~150')
		self._score = value

s = Student()
s.score = 80
print(s.score) # 80
s.score = 125
print(s.score) # 125
# s.score = -125
print(s.score) # score must be 0~150


## 装饰器
## 简单的装饰器函数
# import functools
# def log(func):
# 	@functools.wraps(func)
# 	def wrapper(*args, **kw):
# 		print('log here...',end=' ')
# 		return func(*args, **kw)
# 	return wrapper

# @log
# def now():
# 	print('2017-9-16')

# now() # log here... 2017-9-16

## 带参数装饰器
import functools
def log(text):
	def d(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print(text, end=' ')
			return func(*args, **kw)
		return wrapper
	return d
	

@log('hello world')
def now():
	print('2017-9-16')

now() # hello world 2017-9-16

### 可迭代实例
class Iter():

	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a+self.b
		if self.a > 150:
			raise StopIteration('该结束了，北鼻')
		return self.a

	def __getitem__(self, n):
		a, b = 1, 1
		for i in range(n):
			a, b = b, a+b
		return a

for i in Iter():
	print(i, end=" ") # 1 1 2 3 5 8 13 21 34 55 89 144

print(Iter()[0], Iter()[1], Iter()[2]) # 1 1 2


### 动态属性
class Attr():
	def __init__(self, uri=''):
		self.uri = uri

	def __getattr__(self, path):
		return Attr('{}/{}'.format(self.uri, path))

	def __str__(self):
		return self.uri

	__repr__ = __str__ # 就是简便写法，让repr也返回一样的

print(Attr().C.file.pythonnotes) # /C/file/pythonnotes



#### 反射
class S():
	def __call__(self):
		print('类似 isinstance.method()')

s = S()
s() # 类似 isinstance.method()
