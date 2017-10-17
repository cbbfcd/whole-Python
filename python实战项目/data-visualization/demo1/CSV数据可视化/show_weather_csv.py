# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-10-11 13:51:03
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-11 15:14:01
# @Description: 温度csv数据展示

import matplotlib.pyplot as plt
import csv
import datetime
from matplotlib.dates import MonthLocator, DateFormatter

class ShowWeather(object):
	'''读取并展示csv文件的类'''
	def __init__(self, *args, **kwargs):
		pass


	def read_csv(self, name):
		'''读取csv文件'''
		highs, lows, dates = [], [], []
		with open(r'./'+name, 'r') as f:
			csv_reader = csv.reader(f)
			# 获取第一行头信息
			header = next(csv_reader)
			for data in csv_reader:
				dates.append(data[0])
				highs.append(int(data[1]))
				lows.append(int(data[2]))

		self.show(highs, lows, dates)

	def show(self, highs, lows, dates):
		'''展示天气数据'''
		new_dates = [datetime.datetime.strptime(date, '%Y%m%d') for date in dates]
		# 窗口设置
		plt.figure(figsize=(10, 6))

		# 坐标
		plt.title("温度展示折线图", fontsize=18, fontproperties='SimHei')
		plt.xlabel("日期", fontsize=12, fontproperties='SimHei')
		plt.ylabel("温度", fontsize=12, fontproperties='SimHei')
				
		# 折线图绘制
		plt.plot(new_dates, highs, c='red', linewidth=1, label='最高气温')
		plt.plot(new_dates, lows, c='blue', linewidth=1, label='最低气温')
		plt.fill_between(new_dates, highs, lows, color="gray", alpha=0.5)
		plt.legend(loc="upper left", prop={"family": "SimHei", "size": 12})

		# 日期横坐标格式化
		plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
		plt.gca().xaxis.set_major_locator(MonthLocator())
		plt.gcf().autofmt_xdate()
		plt.savefig('weather_2017.png')

if __name__ == '__main__':
	show = ShowWeather()
	#show.read_csv('weather_2016.csv')
	show.read_csv('weather_2017.csv')
