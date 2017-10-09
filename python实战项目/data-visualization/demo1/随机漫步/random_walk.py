# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-10-07 14:51:07
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-07 15:30:12
# @Description: 随机漫步数据生成类

from random import choice


class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 起点
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步的所有点"""
        while len(self.x_values) < self.num_points:

            # 随机前进的方向和前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的坐标
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
