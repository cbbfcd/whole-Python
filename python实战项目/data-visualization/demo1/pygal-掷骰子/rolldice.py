# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-10-09 10:55:17
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-09 11:21:08
# @Description: 投掷骰子的类

import random

class RollDice():
	'''一个表示投掷骰子的概率统计的类'''

	def __init__(self, points = 6):
		'''骰子的点数'''

		self.points = points


	def roll(self):
		'''投掷骰子'''
		return random.choice(range(1,7))
		