# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-09-26 21:54:24
# @Last Modified by:   28906
# @Last Modified time: 2017-09-27 08:47:10
# @Description: 子弹的类

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''对飞船发射的子弹进行管理的类'''

    def __init__(self, ui_settings, screen, ship):
        '''初始化一个子弹对象'''

        super().__init__()
        self.screen = screen

        # 在(0, 0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(
            0, 0, ui_settings.bullet_width, ui_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储小数表示子弹的位置
        self.y = float(self.rect.y)

        self.color = ui_settings.bullet_color
        self.speed_factor = ui_settings.bullet_speed_factor

    def update(self):
        '''向上移动子弹'''

        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        '''绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)
