# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-09-03 16:25:15
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-03 18:39:47

import pymysql

# 链接数据库
# 参数分别是本地IP，用户名，密码，库名
db = pymysql.connect('localhost','pydb','123456','pytest')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 创建数据库表 
# 使用 execute()方法执行 SQL
cursor.execute('DROP TABLE IF EXISTS USER')

sql = """CREATE TABLE USERS(
			IDCARD VARCHAR(20) NOT NULL,
			NAME VARCHAR(20),
			SEX CHAR(1),
			JOB VARCHAR(20)
		)"""

cursor.execute(sql)
db.close()

# 插入数据
# sql2 = "INSERT INTO USERS VALUES('{}','{}','{}','{}')".format("510154199508187654","lisa","1","saler")
# try:
# 	# 执行
# 	cursor.execute(sql2)
# 	# 提交到数据库执行
# 	db.commit()
# except Exception as e:
# 	# 回滚
# 	print(e)
# 	db.rollback()
# finally:
# 	db.close()
# 	cursor.close()

# 数据库查询操作
# 使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据

# 查询sql
# sql3 = "select * from users where job = '{}'".format('student')

# try:
# 	cursor.execute(sql3)
# except Exception as e:
# 	print('error',e)
# else:
# 	results = cursor.fetchall()
# 	for row in results:
# 		idcard = row[0]
# 		name = row[1]
# 		sex = '男孩' if row[2] == '1' else '女孩'
# 		job = row[3]
# 		print("{}的工作是{},身份证号是{},是个{}".format(name, job, idcard, sex))
# finally:
# 	db.close()
# 	cursor.close()

# 更改操作
# sql4 = "update  users set job = '{}' where name = '{}'".format('teacher', 'Tom')
# try:
# 	# 执行
# 	cursor.execute(sql4)
# 	# 提交到数据库执行
# 	db.commit()
# except Exception as e:
# 	# 回滚
# 	print(e)
# 	db.rollback()
# finally:
# 	db.close()
# 	cursor.close()

# 删除操作
# sql4 = "delete from users  where name = '{}'".format('lisa')
# try:
# 	# 执行
# 	cursor.execute(sql4)
# 	# 提交到数据库执行
# 	db.commit()
# except Exception as e:
# 	# 回滚
# 	print(e)
# 	db.rollback()
# finally:
# 	db.close()
# 	cursor.close()

# mysql-connector-python 的使用，基本一致，请自行百度，我就不过多介绍了
