# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-09-16 14:21:32
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-16 14:55:58

# 一个类案例
class Student():
	'''一个完整的class'''
	# 类属性
	school_name = '成都7中'
	# 私有属性
	__teacher = "miss z"

	# 构造器
	def __init__(self, name, clazz, score, rank, goal):
		self.__name = name
		self.__clazz = clazz
		self.__score = score
		self.__rank = rank
		self.__goal = goal

	def good_news(self):
		print('{}的成绩是{},排名第{},目标是{}'.format(self.__name, self.__score, self.__rank, self.__goal))

	# 成绩是只读属性
	@property
	def score(self):
		print(self.__score)


	# 排名是只读属性
	@property
	def rank(self):
		print(self.__rank)

	@property
	def goal(self):
		print(self.__goal)

	@goal.setter
	def goal(self, g):
		self.__goal = g

	def get_t(self):
		return self.__teacher

	def set_t(self, name):
		self.__teacher = name


s1 = Student('tom','1班',90,5,'年纪前10名')
s2 = Student('jack','1班',98,1,'年纪前3名')
s1.good_news() # tom的成绩是90,排名第5,目标是年纪前10名
s2.good_news() # jack的成绩是98,排名第1,目标是年纪前3名
s1.goal #年纪前10名
s2.goal #年纪前3名
s1.goal ='拿个年纪第一'
s1.goal #拿个年纪第一

print(s1.school_name) # 成都7中
print(s2.school_name) # 成都7中
print(Student.school_name) # 成都7中
s1.school_name = '成都4中'
print(s1.school_name) # 成都4中
print(s2.school_name) # 成都7中
print(Student.school_name) # 成都7中

print(s1.get_t()) # miss z
print(s2.get_t()) # miss z
s1.set_t('miss li')
print(s1.get_t()) # miss li
print(s1._Student__teacher) # miss li
del s1._Student__teacher
print(s1.get_t()) # miss z
print(s2.get_t()) # miss z