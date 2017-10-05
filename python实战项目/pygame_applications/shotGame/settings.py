# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-09-24 22:53:23
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-06 01:00:06
# @Description: 项目通用设置类


class Settings(object):
    '''存储这个游戏的所有基本设置'''

    def __init__(self):
        '''初始化游戏的设置'''
        self.screen_width = 1200  # 屏幕宽
        self.screen_height = 600  # 屏幕高
        self.bg_color = (230, 230, 230)  # 背景色
        # self.ship_speed_factor = 1.5  # 飞船移动速度

        # 子弹的初始化设置
        #self.bullet_speed_factor = 3
        self.bullet_width = 2
        self.bullet_height = 12
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3  # 最大连发数目

        # 外星人初始速度
        #self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # 1右移 -1左移
       #self.fleet_direction = 1

        # 生命值
        self.ship_limit = 3

        # 加快游戏
        self.speed_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """游戏变化设置初始化"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

        # 积分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度"""
        self.ship_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        