# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-10-07 00:53:12
# @Last Modified by:   28906
# @Last Modified time: 2017-10-07 14:22:43
# @Description 绘制简单的折线图

import matplotlib.pyplot as plt

# 输入值
input_value = [1, 2, 3, 4, 5]
# 输出值
squares1 = [1, 4, 9, 16, 25]
squares2 = [1, 8, 27, 16, 125]
# 设置线条宽度、颜色、图列(label)
plt.plot(input_value, squares1, linewidth=2.5, color="orange", label="折线图1")
plt.plot(input_value, squares2, linewidth=2.5, color="steelblue", label="折线图2")
# 图列的位置、以及中文显示
plt.legend(loc="upper left", prop={"family": "SimHei", "size": 12})
# 设置标题、横纵轴标题,支持中文显示
plt.title(u"折线图Demo", fontsize=18, fontproperties='SimHei')
plt.xlabel(u"横坐标", fontsize=12, fontproperties='SimHei')
plt.ylabel(u"纵坐标", fontsize=12, fontproperties='SimHei')

# 刻度的字体也可以设置
plt.tick_params(axis="both", labelsize=12)

plt.show()
