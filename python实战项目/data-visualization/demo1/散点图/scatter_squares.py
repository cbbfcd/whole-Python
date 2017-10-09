# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-10-07 14:26:57
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-07 14:47:48
# @Description: 散点图

import matplotlib.pyplot as plt



# 控制散点的大小、颜色、消除数据点的轮廓(edgecolor)
# 演示绘制1000个点，并且设置颜色映射

x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=5, c=y_values, cmap=plt.cm.Blues, edgecolor="none")
# 设置横纵坐标范围
plt.axis([0, 1100, 0, 1100000])

# 添加标题、横轴纵轴标题
plt.title(u"散点图", fontsize=18, fontproperties='SimHei')
plt.xlabel(u"横坐标", fontsize=12, fontproperties='SimHei')
plt.ylabel(u"纵坐标", fontsize=12, fontproperties='SimHei')

# 设置刻度标记的大小
plt.tick_params(axis="both", which="major", labelsize=10)


plt.show()
