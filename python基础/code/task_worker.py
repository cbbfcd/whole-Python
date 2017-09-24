# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-09-21 22:40:58
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-21 23:15:20


import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class Task(object):
	def __init__(self):
		self.task_que = queue.Queue()    # 任务队列
		self.result_que = queue.Queue()  # 结果队列

	def start(self):
		# 注册队列
		BaseManager.register("get_task_queue")
		BaseManager.register("get_result_queue")

		# 连接master
        server = '127.0.0.1'
        manager = BaseManager(address=(server, 8888), authkey=b'abc')
        manager.connect()

        # 使用网络服务获取上面的队列，不能直接获取
		task_queue = manager.get_task_queue()
		result_queue = manager.get_result_queue()

		# run
		for i in range(10):
			r = task_queue.get(timeout=1)
			r += '--> 结果'
			print(r)
			result_queue.put(r)
if __name__ == '__main__':
	ts = Task()
	ts.start()


