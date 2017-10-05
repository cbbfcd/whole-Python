# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-09-29 22:47:55
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-06 01:27:36
# @Description: 跟踪游戏的统计信息

class GameStats():
	"""游戏统计"""
	def __init__(self, ui_settings):
		"""初始化统计信息"""
		self.ui_settings = ui_settings
		self.reset_stats()
		# 游戏状态
		self.game_active = False
		self.score = 0
		# 记录最高得分
		self.high_score = 0

	def reset_stats(self):
		"""初始化在游戏运行期间可能变化的统计信息"""
		self.ships_left = self.ui_settings.ship_limit
		self.score = 0