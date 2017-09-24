# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-09-21 22:28:02
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-21 23:09:46


## 主任务
import random, time, queue
from multiprocessing.managers import BaseManager
class Master(object):

	def __init__(self):
		self.task_que = queue.Queue()    # 任务队列
		self.result_que = queue.Queue()  # 结果队列

	def get_task_que(self):
		return self.task_que

	def get_result_que(self):
		return self.result_que

	def start(self):
		# 注册队列
		BaseManager.register("get_task_queue",callable=self.get_task_que)
		BaseManager.register("get_result_queue",callable=self.get_result_que)

		# 监听
		manager = BaseManager(address=('0.0.0.0', 5000), authkey=b'abc')
		manager.start()

		# 使用网络服务获取上面的队列，不能直接获取
		task_queue = manager.get_task_queue()
		result_queue = manager.get_result_queue()

		# 设置任务
		for i in range(10):
			r = '任务' + i
			task_queue.put(r)

		# 监听result
		for i in range(10):
			res = result_queue.get()
			print('res is {}'.format(res))

		manager.shutdown()

if __name__ == '__main__':
	m = Master()
	m.start()
