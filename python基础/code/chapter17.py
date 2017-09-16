# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-09-17 00:57:16
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-17 01:33:07


# type()动态创建一个类

def fn(self, name='Tom'):
	print('Hello, {}'.format(name))

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
s = Hello()
s.hello() # Hello, Tom
print(type(s)) # <class '__main__.Hello'>
print(type(Hello)) # <class 'type'>


class ListMetaClass(type): #=> 必须继承type
	def __new__(cls, name, bases, fns):
		fns['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, fns)

class myList(list, metaclass=ListMetaClass):
	pass

L = myList()
L.add(1)
print(L) #[1]