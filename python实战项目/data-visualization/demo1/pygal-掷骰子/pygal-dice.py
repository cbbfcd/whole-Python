# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-10-09 11:04:46
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-09 11:24:02
# @Description: 投掷骰子的可视化

import pygal
from rolldice import RollDice


rolldice = RollDice()
result = []
count = 0
data = []

# 统计数据
while True:
	n = rolldice.roll()
	result.append(n)
	if count >= 1000:
		break
	count += 1

if len(result):
	for i in range(1,7):
		ns = result.count(i)
		data.append(ns)


# 可视化
hist = pygal.Bar()
hist.title = "roll dice counts"
hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist.x_title = "numbers"
hist.y_title = "count numbers"

hist.add("RollDice", data)
hist.render_to_file(r'./die_visual.svg')