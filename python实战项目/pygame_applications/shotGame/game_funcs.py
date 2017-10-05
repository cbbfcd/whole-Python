# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-09-26 00:24:54
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-06 01:40:48
# @Description: 事件模块

import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(ui_settings, screen, stats,sb, play_button, ship, aliens, bullets):
    '''响应鼠标和键盘事件'''

    # 监听键盘和鼠标事件
    for event in pygame.event.get():
        # 监听退出事件
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ui_settings, screen, stats,sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

        # 监听左右箭头事件
        check_keydown_events(event, ui_settings, screen, ship, bullets)
        check_keyup_events(event, ship)


def check_play_button(ui_settings, screen, stats,sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """点击start开启游戏"""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        # 重置信息
        stats.reset_stats()
        stats.game_active = True

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人
        create_fleet(ui_settings, screen, ship, aliens)
        ship.center_ship()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 初始游戏设置
        ui_settings.initialize_dynamic_settings()

        # 重置积分
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_ships()


def update_screen(ui_settings,stats, sb,  screen, ship, aliens, bullets, play_button):
    '''更新屏幕上的图像，并切换到新的屏幕'''
    # 每次循环都重绘屏幕
    screen.fill(ui_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)

    # 显示得分
    sb.show_score()

    # 如果游戏状态非活动，就绘制按钮
    if not stats.game_active:
        play_button.draw_button()

    # 重绘所有子弹
    for bullet in bullets:
        bullet.draw_bullet()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def check_keydown_events(event, ui_settings, screen, ship, bullets):
    '''键盘按下的事件'''
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            fire_bullet(ui_settings, screen, ship, bullets)
        elif event.key == pygame.K_q:
            sys.exit()


def check_keyup_events(event, ship):
    '''松开按键的事件'''
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False


def check_bullet_alien_collisions(ui_settings, screen,stats,sb, ship, aliens, bullets):
    """响应子弹和外星人的碰撞"""
    # 通过碰撞检测，检查是不是击中了外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ui_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    # 外星人没有了就继续创建
    if len(aliens) == 0:
        bullets.empty()
        ui_settings.increase_speed()
        create_fleet(ui_settings, screen, ship, aliens)


def update_bullets(ui_settings, screen,stats,sb, ship, aliens, bullets):
    '''子弹的事件管理'''
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ui_settings, screen,stats,sb, ship, aliens, bullets)


def fire_bullet(ui_settings, screen, ship, bullets):
    '''开火的函数'''
    # 创建一个子弹，并加入编组中
    if len(bullets) < ui_settings.bullet_allowed:
        new_bullet = Bullet(ui_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ui_settings, alien_width):
    """计算每行可以容纳多少个外星人"""
    available_space_x = ui_settings.screen_width - 2 * alien_width
    numbers_alien_x = int(available_space_x / (2 * alien_width))
    return numbers_alien_x


def get_number_rows(ui_settings, ship_height, alien_height):
    """计算可以容纳多少行外星人"""
    available_space_y = (ui_settings.screen_height -
                         3 * alien_height - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ui_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人"""
    alien = Alien(ui_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ui_settings, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(ui_settings, screen)
    alien_width = alien.rect.width
    numbers_alien_x = get_number_aliens_x(ui_settings, alien_width)
    number_rows = get_number_rows(
        ui_settings, ship.rect.height, alien.rect.height)
    # 外星人群
    for row_number in range(number_rows):
        for alien_number in range(numbers_alien_x):
            create_alien(ui_settings, screen, aliens, alien_number, row_number)


def check_fleet_direction(ui_settings, aliens):
    """整群外星人下移并改变方向"""
    for alien in aliens:
        alien.rect.y += ui_settings.fleet_drop_speed
    ui_settings.fleet_direction *= -1


def check_fleet_edges(ui_settings, aliens):
    """有外星人到达边缘的时候采取的措施"""
    for alien in aliens:
        if alien.check_edges():
            check_fleet_direction(ui_settings, aliens)
            break


def ship_hit(ui_settings, stats,sb, screen, ship, aliens, bullets):
    """响应外星人撞到的飞船"""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人
        create_fleet(ui_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ui_settings, stats,sb, screen, ship, aliens, bullets):
    """检查外星人是不是到达底部"""
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ui_settings, stats,sb, screen, ship, aliens, bullets)
            break


def update_aliens(ui_settings, stats,sb, screen, ship, aliens, bullets):
    """更新所有外星人的位置"""
    check_fleet_edges(ui_settings, aliens)
    aliens.update()
    check_aliens_bottom(ui_settings, stats,sb, screen, ship, aliens, bullets)
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ui_settings, stats,sb, screen, ship, aliens, bullets)

def check_high_score(stats, sb):
    """检查是否诞生了最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

