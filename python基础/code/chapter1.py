# -*- coding: utf-8 -*-
# @Author: huangteng
# @Date:   2017-08-10 15:52:07
# @Last Modified by:   28906
# @Last Modified time: 2017-08-18 11:42:21
# @Description: python基础一之 数据结构与变量、基本运算
# @version:
import math
import random

# 算术运算
a, b = 21, 22
print( a + b ) #加 43
print( a - b ) #减 -1
print( a * b ) #乘 462
print( a ** b ) #乘方 122694327386105632949003612841
print( a / b ) #除 0.9545454545454546 整数与浮点数相除等到的是浮点数。
print( a // b ) #整除 0 得到的是整数


# 比较运算
c, d = 10, 15
print( c == d ) # False
if c <= d:
	print('{}小于{}'.format(c, d))


# 位运算符
a1 = 60            # 60 = 0011 1100 
b1 = 13            # 13 = 0000 1101 
c1 = 0
 
c1 = a1 & b1;        # 12 = 0000 1100
print ("1 - c1 的值为：", c1)
 
c1 = a1 | b1;        # 61 = 0011 1101 
print ("2 - c1 的值为：", c1)
 
c1 = a1 ^ b1;        # 49 = 0011 0001
print ("3 - c1 的值为：", c1)
 
c1 = ~a1;           # -61 = 1100 0011
print ("4 - c1 的值为：", c1)
 
c1 = a1 << 2;       # 240 = 1111 0000
print ("5 - c1 的值为：", c1)
 
c1 = a1 >> 2;       # 15 = 0000 1111
print ("6 - c1 的值为：", c1)


# 成员运算符

if 1 in [1,2]:
	print('hello, {}'.format(1))


# 身份运算符

# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等

f, g, h, l = 10, 10, {'a':2}, {'a':2}
if f is g:
	print('{}和{}有相同的标识'.format(f, g))
if id(h) != id(l):
	print('{}和{}引用地址不同'.format(h, l))
if h == l:
	print('{}和{}有相同的值'.format(h, l))
if h is l:
	print('{}和{}有相同的引用地址'.format(h, l))


# 类型判断

class A:
	pass

class B(A):
	pass

print(type(A()) == A) # true
print(type(B()) == A) # false
print(isinstance(A(), A)) # true
print(isinstance(B(), A)) # true

# Number类型

Num1 = 5
print(Num1)
del Num1
# print(Num1) 报错Num1没有定义  因为del语句删除一些数字对象的引用

Num2 =  .5
print(int(Num2)) # 0



max1 = max([1,2,3])
print(max1) # 3
print(pow(2,5))

# 随机数
r1 = random.choice([1,22,3,56])
print(r1)
print(math.floor(100*random.random()))
lists = [1,2,3,4,5,6];random.shuffle(lists);print(lists)

# 字符串

str2 = 'hello world'
print(str2[0:2]) # he
print(str2[:6]) # hello 
print(str2[:-3]) # hello wo
print(str2*2) # hello worldhello world

# 转义、原始字符串
str1 = 'i\'m jack'
rstr1 = r'i\'m jack'
print(str1) # i'm jack
print(rstr1) # i\'m jack

# str1[0]='h' # 报错， 字符串是不可改变的
str1_new = 'h' + str1[1:]
print(str1_new) # h'm jack

print('i\'m a student,\000 so, \r what are you doing? \t haha')


# 字符串运算
s1 = 'hello'
if 'h' in s1:
	print(s1*2 + s1[0:2]) # hellohellohe
if 'p' not in s1:
	print(r'{} not in {}'.format('p', s1)) # p not in hello

# 字符串格式化
print('this is a %s who age is %d' % ('guy',52)) # this is a guy who age is 52
print('this num is %.2f' % 15.232323) # this num is 15.23
print('this num is {:.3f}'.format(15.232323)) # this num is 15.232
print('this num is {:,}'.format(15232323)) # this num is 15,232,323

# 多行字符串
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

# 字符串函数
fstr = 'hello world'
cstr = '中文'
# capitalize(str) 首字母大写
print(fstr.capitalize()) # Hello world

# center(width,filter) 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格
# width不够 原样返回字符串
print(fstr.center(15, '_')) # __hello world__

# count(str, beg= 0,end=len(string))
# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
print(fstr.count('l')) # 3

# encode/decode
# 编码/解码
e_str = cstr.encode('utf-8')
print(e_str) # b'\xe4\xb8\xad\xe6\x96\x87'
# Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象
print(e_str.decode('utf-8')) # 中文
# 可以粗解为通过encode把字符串编码成指定编码格式的 bytes 对象，
# 然后通过 decode 来解码成我们需要的编码格式的字符串，主要用来处理中文乱码的问题较多。

# endswith(suffix, beg=0, end=len(string))
# 是否是以suffix结束，返回布尔值
print(fstr.endswith('ld')) # True
print(fstr.endswith('ld', 1, 5)) # False

# expandtabs(tabsize=8)
# 把字符串 string 中的 tab 符号转为空格
print('tt\tt'.expandtabs()) # tt      t

# find(str, beg=0 end=len(string))
# 检测 str 是否包含在字符串中，找到第一个即返回，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，
# 如果是返回开始的索引值，否则返回-1
# rfind()  从右开始找
print(fstr.find('l')) # 2
print(fstr.find('helld')) # -1
print(fstr.find('world', -1, -11)) # -1

# index(str, beg=0, end=len(string))
# 同find,唯一不同的是找不到的话，index函数会报异常
# rindex()  从右开始找
print(fstr.index('l')) # 2
# print(fstr.index('m')) # 报错

# isalnum()
# 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
# 必须包含字母和数字,空格什么的都不能有
print(fstr.isalnum()) # False
print('a4'.isalnum()) # True

# isalpha()
# 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
# 只能有字母,空格什么的都不能有
print(fstr.isalnum()) # False
print('a4'.isalnum()) # True

# isdigit()
# 只能有数字，字母、空格什么的不能有
print('4 4'.isalnum()) # False
print('a4'.isalnum()) # True
print('54.132'.isalnum()) # False

# islower()
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写
print('abc'.islower(), 'test') # True test
print('abc d'.islower(), 'test') # True test
print('abc4 d'.islower(), 'test') # True test
print('Abc4 d'.islower(), 'test') # False test
print('aBc4 d'.islower(), 'test') # False test

# isnumeric()
# 只包含数字
print('456'.isnumeric()) # True
print('456 7'.isnumeric()) # False


# isspace()
# 只包含空白
print(' '.isspace()) # True
print(' a'.isspace()) # False

# istitle()
# 是否是标题格式的
print('AaBb'.istitle()) # False
print("Ac Bs".istitle()) # True

# isupper()
# 包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写
print('123'.isupper()) # False
print('ab c'.isupper()) # False
print('Abc'.isupper()) # False
print('A'.isupper()) # True

# join(seq)
# 以指定字符串,join一个序列
print('__'.join(('1', '2', '3'))) # 1__2__3
print('**'.join(['1', '2'])) # 1**2

# len(string)
# 返回字符串长度
print(len('123')) # 3

# ljust(width[, fillchar]) /  rjust(width[, fillchar])   
# 返回左/右对齐字符串，参数是长度和填充字符
print('567'.ljust(4,'*')) # 567*
print('567'.rjust(4,'*')) # *567

# lower()
# 小写
print('ABCd'.lower()) # abcd

# lstrip()  rstrip() strip()
# 截掉左      右       两边 的空格
print(' abc'.lstrip()) # abc
print(' abc '.strip()) # abc 

# replace(old, new [, max])
# 替换，max指的是最多替换次数
print('abca'.replace('a','_a',1)) # _abca
print('abca'.replace('a','_a',2)) # _abc_a

# split(str="", num=string.count(str))  str不能写'' 默认为所有的空字符，包括空格、换行(\n)、制表符(\t)
# 字符串分割
print('1234'.split()) # ['1234']
print('1 2 3 4'.split()) # ['1', '2', '3', '4']
print('1,2,34'.split( ',' )) # ['1', '2', '34']

# startswith(str, beg=0,end=len(string))
# 检查是否是以str开头
print('hello'.startswith('h')) # True
print('hello'.startswith('h',1)) # False

# swapcase()
# 大写转小写， 小写转大写
print('hELLO'.swapcase()) # Hello

# title()
# 驼峰
print('abc'.title()) #Abc
print('abc def'.title()) #Abc Def

# upper()
# 大写

# isdecimal()
# 是否只包含十进制
print('123'.isdecimal()) # True

# 列表
list1 = [1, '2', '3']
list2 = list1 * 2
print(list1 + list2) # [1, '2', '3', 1, '2', '3', 1, '2', '3']
print(list1[1:]) # ['2', '3']
print(list2[-5:]) # ['2', '3', 1, '2', '3']
list1[0] = 12
print(list1) # [12, '2', '3']


# 列表操作函数
__list = [1, 2, 2,]
# len() 长度
print('长度是 %d' % (len(__list))) # 长度是 3
# max() min() 最大最小值
print('最大值:%d,最小值:%d' % (max(__list), min(__list))) # 最大值:2,最小值:1
# list() 元组转列表
print(type((1,2,3))) # <class 'tuple'>
print(type(list((1,2,3)))) # <class 'list'>
# append() 队尾添加
__list.append(3);print(__list) # [1, 2, 2, 3]
# count() 统计出现次数
print('出现次数: {}'.format(__list.count(2))) # 出现次数: 2
__list2 = ['a', 'b']
# extend() 在队尾合并列表
__list.extend(__list2);print(__list) # [1, 2, 2, 3, 'a', 'b']
# index() 返回索引，只找一次
print(__list.index('a')) # 4
# insert(i,x) 其实就是list[i]=x
__list.insert(0, '哈');print(__list) # ['哈', 1, 2, 2, 3, 'a', 'b']
# pop(i) 删除并返回索引为 i 的元素 ,默认从队尾删除
# 等同于 del list[i]
print(__list.pop()) # b
print(__list.pop(0)) # 哈
# remove(x) 从头删除第一个 x，不返回值
__list.remove('a');print(__list) # [1, 2, 2, 3]
# reverse() 反转
__list.reverse();print(__list) # [3, 2, 2, 1]
# sort() 排序
__list.sort();print(__list) # [1, 2, 2, 3]
# copy() 拷贝
__list3 = __list.copy()
print('拷贝列表',__list3) # 拷贝列表 [1, 2, 2, 3]
__list3[0]='aa'
print(__list, __list3) #[1, 2, 2, 3] ['aa', 2, 2, 3]
# clear() 清除
__list3.clear();print(__list3) # []



# 列表解析
print([n*n for n in range(1,11)]) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 传统写法
_list_ = []
for n in range(1, 11):
	_list_.append( n*n )
print(_list_)

# 还可以有逻辑判断
# 1. 筛选出大于0的
_num_list = [-1, 34, -5, 68, 7, 0, -4]
print([n for n in _num_list if n > 0]) # [34, 68, 7]

#2. 选出含有 'a' 的
_word_list = ['am', 'test', 'apoll', 'tt']
print([n for n in _word_list if 'a' in n]) # ['am', 'apoll']



# 元组
_tuple = (1)
print(type(_tuple)) # <class 'int'>

_tuple=(1,)
print(type(_tuple)) # <class 'tuple'>

# _tuple[0] = '1' # 报错，tuple不可变
_tuple2 = ('1',) + _tuple[1:]
print(_tuple2) # ('1',)

print(_tuple2 * 2 ) # ('1', '1')
print('1' in _tuple) # False
print(1 in _tuple) # True

_multi_tuple = (1, '1', (1,), [1, 3])

# del _multi_tuple[0]

print(_multi_tuple[-2:]) # ((1,), [1, 3])

_multi_tuple[-1][0] = '哈'
print(_multi_tuple[-2:]) # ((1,), ['哈', 3])


# 元组的内置函数
_tem = (0, 1, 2, 3, '4')

# len() 计算长度
print(len(_tem)) # 5

# max(tuple) min() 最大最小值
# print(max(_tem), min(_tem)) # 报错 因为有个 string

# tuple() 列表转元祖
print(type(tuple([1,]))) # <class 'tuple'>

# .count() 统计次数
print(_tem.count('4')) # 1

# .index(x) 查找x的第一个出现的索引，找不到会报错哦
print(_tem.index('4')) # 4


# 集合
colors = {'white', 'red', 'blue', 'red'}
days = set('abcdefggggg')
print('colors: {}'.format(colors)) # colors: {'white', 'blue', 'red'} 去除了重复,且无序
print('days: {}'.format(days)) # days: {'d', 'g', 'f', 'c', 'a', 'b', 'e'}

# 创建空集合要用 set()
print(type({})) # <class 'dict'>
print(type(set())) # <class 'set'>

# set可以进行集合运算
set1 = {'a', 'b', 'c'}
set2 = {'b', 'c', 'd', 'e'}
print( set1 - set2 ) # {'a'}
print( set2 - set1 ) # {'e', 'd'}

print( set1 ^ set2) # {'e', 'a', 'd'}           两个的差集
print( set1 & set2) # {'c', 'b'}                两个的交集
print( set1 | set2) # {'a', 'b', 'c', 'e', 'd'} 两个的并集

# 字典
obj = {'a':123}
obj['b'] = 124
print('obj: {}'.format(obj)) # obj: {'b': 124, 'a': 123}
print('keys: {}'.format(obj.keys())) # keys: dict_keys(['b', 'a'])
print('values: {}'.format(obj.values())) # values: dict_values([123, 124])
aa=list(obj.keys()) # dict_values 转成 列表才可以有那些操作哦
print(aa[0]) # a


# 字典常用函数
dict1 = {'a': 123, 'b': 321}

# dict.clear() 清除字典内的所有元素
obj.clear();print(obj) # {}

# dict.copy() 浅拷贝
#     1. == 比较的是值, is 比较的地址
#     2. 浅拷贝拷贝的是值，而不是引用地址
dict2 = dict1.copy()
print(dict1 == dict2) # True
print(dict1 is dict2) # False
dict2['b'] = 654
print(dict1, dict2) # {'b': 321, 'a': 123} {'b': 654, 'a': 123}
print(dict1 == dict2) # False

# dict.get(key, default=None) 返回指定键的值，如果值不在字典中返回default值
print(dict1.get('a')) # 123
print(dict1.get('g','没有这个key')) # 没有这个key

# key in dict 如果键在字典dict里返回true，否则返回false
print('a' in dict1)  # True

# dict.keys() dict.values() dict.items() 这里讲讲items就好了
# 返回一个列表，形式大概是 [(key,value),(key,value)]
items = list(dict1.items())
print(items) # [('a', 123), ('b', 321)]
print(items[0][0]) # a 这个结果不稳定的，因为返回的tuple顺序不固定

# dict.update(dict2) 把dict2更新到dict
# 键相同的话会覆盖，没有则是新增
dict1.update({'e':999, 'a':123.3})
print(dict1) # {'b': 321, 'a': 123.3, 'e': 999}

# pop(key[,default]) 删除字典给定键 key 所对应的值，返回值为被删除的值。
# key值必须给出。 否则，返回default值。
print(dict1.pop('a')) # 123.3
print(dict1) # {'b': 321, 'e': 999}

# popitem()
# 随机删除一对键值对
print(dict1.popitem())
print(dict1)
