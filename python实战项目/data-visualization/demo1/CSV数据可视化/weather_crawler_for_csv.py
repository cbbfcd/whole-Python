# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-10-11 10:10:35
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-10-11 14:12:45
# @Description: 爬取成都16，17年 1-9月份天气数据，并转存为csv格式文件
import requests
import json
import csv


class Weather_CSV(object):
    '''爬取成都是16，17年 1-9月份天气数据，并转存为csv格式文件的类'''

    def __init__(self):
        pass

    def request(self, url):
        '''请求数据'''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.35',
            'Referer': 'http://www.weather.com.cn/weather40d/101270101.shtml'
        }

        return requests.get(url, headers=headers)

    def create_url(self, base='http://d1.weather.com.cn/calendar_new/'):
        '''生成访问的地址'''
        years, months = ['2016', '2017'], [
            '0' + str(x) for x in range(1, 13) if x < 10] + [str(x) for x in range(1, 13) if x >= 10]
        url1, url2, urls = [], [], []
        for year in years:
            for month in months:
                url = base + year + '/101270101_' + year + month + '.html'
                if year == '2016':
                    url1.append(url)
                else:
                    url2.append(url)

        urls.append(url1)
        urls.append(url2)

        return urls

    def fetchData(self):
        '''爬取数据'''
        self.write_csv_header('weather_2016.csv')
        self.write_csv_header('weather_2017.csv')
        urls = self.create_url()
        self.saveToCsv('weather_2016.csv', urls[0])
        self.saveToCsv('weather_2017.csv', urls[1])

    def write_csv_header(self, name):
        '''csv文件头'''
        with open(r'./' + name, 'w', newline='') as f:
            f_writer = csv.writer(f)
            f_writer.writerow(['日期', '最高气温', '最低气温'])

    def saveToCsv(self, name, urls):
        '''存储为csv文件'''
        for url in urls:
            res = self.request(url).content
            json_str = res.decode('utf-8')[11:]
            weathers = json.loads(json_str)
            for weather in weathers:
                data = [weather.get('date'), weather.get(
                    'hmax'), weather.get('hmin')]
                with open(r'./' + name, 'a', newline='') as f:
                    f_writer = csv.writer(f)
                    f_writer.writerow(data)

if __name__ == '__main__':
    weather = Weather_CSV()
    weather.fetchData()
