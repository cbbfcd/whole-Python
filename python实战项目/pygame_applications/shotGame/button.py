# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-10-05 23:57:13
# @Last Modified by:   28906
# @Last Modified time: 2017-10-06 00:08:13

import pygame.font


class Button(object):

    def __init__(self, ui_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 按钮设置
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 按钮位置
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮只需要创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """渲染msg"""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制按钮"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
