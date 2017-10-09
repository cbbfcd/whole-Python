# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-10-07 15:31:29
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-07 15:50:06
# @Description: 随机漫步的可视化图

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 创建随机漫步的可视化图
rw = RandomWalk()
rw.fill_walk()
# 设置绘制窗口的尺寸
plt.figure(figsize=(10, 6))

# 绘制
plt.scatter(rw.x_values, rw.y_values, s=5, c=list(range(rw.num_points)), cmap=plt.cm.Blues, edgecolor="none")
# 突出起点和终点
plt.scatter(0, 0, c="orange", edgecolors="none", s=10)
plt.scatter(rw.x_values[-1], rw.y_values[-1], edgecolors="none", c="red", s=10)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)



# 添加标题、横轴纵轴标题
plt.title(u"随机漫步图", fontsize=18, fontproperties='SimHei')
plt.xlabel(u"横坐标", fontsize=12, fontproperties='SimHei')
plt.ylabel(u"纵坐标", fontsize=12, fontproperties='SimHei')

# 设置刻度标记的大小
plt.tick_params(axis="both", which="major", labelsize=10)
plt.show()

