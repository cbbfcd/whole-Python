# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-10-11 21:11:34
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-11 22:15:55
# @Description: 获取github上的数据

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

language = 'javascript'
res_dicts = []
# url = 'https://api.github.com/search/repositories?q=language:{}&sort=stars&page={}'.format(language,page)
for i in range(1, 3):
	r = requests.get('https://api.github.com/search/repositories?q=language:{}&sort=stars&page={}'.format(language,i))
	res = r.json()
	res_dicts += res['items']
# r = requests.get(url)

# res = r.json()
# res_dicts = res['items']

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.width = 1200

names, plot_dicts = [], []
for res_dict in res_dicts:
	names.append(res_dict['name'])
	plot_dict = {
		'value': res_dict['stargazers_count'],
		'label': str(res_dict['description'])[:200]+'...',
		'xlink': res_dict['html_url']
	}
	plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most Star {} Project on GitHub'.format(language)
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')


