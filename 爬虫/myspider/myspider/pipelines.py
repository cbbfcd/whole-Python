# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import copy
from twisted.enterprise import adbapi


class MyspiderPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            db=settings['MYSQL_DBNAME'],
			charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False
        )

    # 连接池
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        return cls(dbpool)

    def process_item(self, item, spider):
        asyncitem = copy.deepcopy(item)
        q = self.dbpool.runInteraction(self.do_insert, asyncitem)
        q.addErrback(self.handle_error)

    def do_insert(self, cursor, item):
        insert_sql, params = item.get_insert_sql()
        cursor.executemany(insert_sql, [params])
        
    def handle_error(self, err):
        print('..................err..................')
        print(err)


