# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-09-24 22:15:09
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-06 01:39:07
# @Description: 游戏窗口

import pygame
from pygame.sprite import Group
from settings import Settings
import game_funcs as gf
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏
    pygame.init()
    ui_settings = Settings()
    # 创建一个窗口
    screen = pygame.display.set_mode(
        (ui_settings.screen_width, ui_settings.screen_height))
    # 设置窗口标题
    pygame.display.set_caption('Shot Game')
    # 绘制飞船
    ship = Ship(ui_settings, screen)
    # 子弹编组,可以给编组内元素统一执行事件。
    bullets = Group()
    # 绘制外星人
    alien = Alien(ui_settings, screen)
    # 外星人编组
    aliens = Group()
    gf.create_fleet(ui_settings, screen, ship, aliens)
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ui_settings)
    # 绘制开始按钮
    play_button = Button(ui_settings, screen, "Start")
    # 绘制得分
    sb = Scoreboard(ui_settings, screen, stats)

    # 开始游戏的主循环
    while True:
        gf.check_events(ui_settings, screen, stats,sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ui_settings, screen,stats,sb, ship, aliens, bullets)
            gf.update_aliens(ui_settings, stats,sb, screen, ship, aliens, bullets)
        gf.update_screen(ui_settings,stats, sb,  screen, ship, aliens, bullets, play_button)

run_game()
