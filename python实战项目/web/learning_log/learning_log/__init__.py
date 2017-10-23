# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-10-17 22:43:15
# @Last Modified by:   28906
# @Last Modified time: 2017-10-17 23:07:32
# @Description: '初始化配置'
import pymysql
pymysql.install_as_MySQLdb()

# 打开数据库链接
db = pymysql.connect("localhost", "pydb", "123456", "oic")

# 获取游标操作
cursor = db.cursor()

# 使用execute执行sql
cursor.execute("SELECT VERSION()")

# 使用fetchone获取一条数据
data = cursor.fetchone()

print("Mysql Version is {}".format(data))

# 关闭数据库连接
db.close()


