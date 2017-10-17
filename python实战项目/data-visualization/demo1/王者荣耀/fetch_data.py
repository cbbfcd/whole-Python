# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-10-12 16:55:58
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-12 17:46:22
# @Description: 获取王者荣耀所有英雄的数据
import requests
import json
class FetchKOGData():

	'''获取王者荣耀数据的类'''
	def __init__(self):
		pass

	def fetch_get(self, url, headers):
		'''获取数据的get方法'''
		return requests.get(url, headers=headers)

	def get_hero_data(self):
		'''获取所有英雄的数据'''
		url = 'http://kogapi.games-cube.com/champion'
		headers={
			'DAIWAN-API-TOKEN':'00F82-CE628-2A142-A77CE'
		}
		data = self.fetch_get(url, headers).json()
		
		with open(r'./hero_data.json','w', encoding='utf-8') as f:
			json.dump(data, f, ensure_ascii=False, indent=4)
			f.write('')

if __name__ == '__main__':
	fetchKogData = FetchKOGData()
	fetchKogData.get_hero_data()


