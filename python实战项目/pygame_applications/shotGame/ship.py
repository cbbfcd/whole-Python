# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-09-24 23:23:56
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-29 23:00:34
# @Description: 飞机模块
import pygame


class Ship(object):
    '''集中管理飞机的一个类'''

    def __init__(self, ui_settings, screen):
        '''初始化飞机，设置其初始位置'''
        self.screen = screen
        self.ui_settings = ui_settings

        # 加载飞船图像
        self.image = pygame.image.load('imgs/ship.bmp')
        # 获取飞船外接矩形
        self.rect = self.image.get_rect()
        # 获取屏幕外接矩形
        self.screen_rect = screen.get_rect()

        # 将飞机放在屏幕水平居中
        self.rect.centerx = self.screen_rect.centerx
        # 在飞船的属性中存储小数
        self.center = float(self.rect.centerx)
        # 将飞机放在屏幕底部
        self.rect.bottom = self.screen_rect.bottom
        # 飞船右移动的标志
        self.moving_right = False
        # 飞船左移动的标志
        self.moving_left = False

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''根据移动标志移动飞船的位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ui_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ui_settings.ship_speed_factor
        self.rect.centerx = self.center

    def center_ship(self):
        """让飞船居中"""
        self.center = self.screen_rect.centerx
        