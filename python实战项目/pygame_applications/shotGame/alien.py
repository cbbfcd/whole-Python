# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-09-29 21:25:05
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-29 22:26:23
# @Description: 外星人类

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ui_settings, screen):
        """外星人初始化"""
        super().__init__()
        self.screen = screen
        self.ui_settings = ui_settings

        # 加载外星人图像
        self.image = pygame.image.load('imgs/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初的位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """如果外星人位于屏幕边缘就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向左或者右移动外星人"""
        self.x += self.ui_settings.alien_speed_factor * self.ui_settings.fleet_direction
        self.rect.x = self.x
