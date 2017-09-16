# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-09-17 01:36:33
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-17 02:46:36


# 1. super

# 单继承
class A(object):

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def sayHello(self):
		print('this is class A, a={},b={}'.format(self.a, self.b))

class B(A):

	def __init__(self, a, b, c):
		super(B, self).__init__(a,b)
		self.c = c

	def sayHello(self):
		super(B, self).sayHello() 
		print('this is b call')

b = B('b','also b','test')
b.sayHello() 
# this is class A, a=b,b=also b
# this is b call



# 多重继承

class D(object):
	def __init__(self):
		print('enter D')
		super(D, self).__init__()
		print('out D')

class Base(object):
	def __init__(self):
		print('enter Base')
		print('out Base')
class A(Base):
	def __init__(self):
		print('enter A')
		super(A, self).__init__()
		print('out A')
class B(Base):
	def __init__(self):
		print('enter B')
		super(B, self).__init__()
		print('out B')
class C(A, B):
	def __init__(self):
		print('enter C')
		super(C, self).__init__()
		print('out C')

c = C()
#enter C
#enter A
#enter B
#enter Base
#out Base
#out B
#out A
#out C

print(C.mro())
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]


# 避免重复
class E(object):
	def __init__(self):
		print('enter E')
		print('out E')
class F(E):
	def __init__(self):
		print('enter F')
		E.__init__(self)
		print('out F')
class G(F, E):
	def __init__(self):
		print('enter G')
		F.__init__(self)
		E.__init__(self)
		print('out G')
g = G()
# enter G
# enter F
# enter E
# out E
# out F
# enter E
# out E
# out G