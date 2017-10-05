# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-10-06 00:36:05
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-06 01:48:26

import pygame.font
from pygame.sprite import Sprite
from pygame.sprite import Group
from ship import Ship

class Scoreboard(Sprite):

    def __init__(self, ui_settings, screen, stats):
        """初始化"""
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.ui_settings = ui_settings
        self.stats = stats

        # 显示得分字体
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 得分图像
        self.prep_score()
        self.prep_high_score()

        # 剩余飞船
        self.prep_ships()

    def prep_score(self):
        """显示得分的图像"""
        round_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(round_score)
        self.score_img = self.font.render(score_str, True, self.text_color, self.ui_settings.bg_color)

        # 将得分放在右上角
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
    	"""绘制得分"""
    	self.screen.blit(self.score_img, self.score_rect)
    	self.screen.blit(self.img_high_score, self.high_score_rect)
    	self.ships.draw(self.screen)

    def prep_high_score(self):
    	"""记录最高得分"""
    	high_score = int(round(self.stats.high_score, -1))
    	high_score_str = "{:,}".format(high_score)
    	self.img_high_score = self.font.render(high_score_str, True, self.text_color, self.ui_settings.bg_color)


    	self.high_score_rect = self.img_high_score.get_rect()
    	self.high_score_rect.centerx = self.screen_rect.centerx
    	self.high_score_rect.top = self.screen_rect.top

    def prep_ships(self):
    	"""显示还剩飞船数目"""
    	self.ships = Group()

    	for ship_number in range(self.stats.ships_left):
    		ship = Ship(self.ui_settings, self.screen)
    		ship.rect.x = int(10 + ship_number * ship.rect.width)
    		ship.rect.y = 5
    		self.ships.add(ship)