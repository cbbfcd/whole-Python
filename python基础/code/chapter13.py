# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-09-05 19:52:22
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-20 23:28:04


# 多线程


# 首先我们模拟一下单任务的情景
# from time import ctime, sleep

# def _music1(musicName):
# 	print('我在听{},时间: {}'.format(musicName, ctime()))
# 	sleep(2)

# def _movies(movieName):
# 	print('我在看{},时间: {}'.format(movieName, ctime()))
# 	sleep(4)

# def main1():
# 	_music1('老子明天不上班')
# 	_movies('战狼2')
# 	print('all over {}'.format(ctime()))


# if __name__ == '__main__':
# 	main1()
# 输出结果
# 我在听老子明天不上班,时间: Tue Sep  5 20:29:46 2017
# 我在看战狼2,时间: Tue Sep  5 20:29:48 2017
# all over Tue Sep  5 20:29:52 2017
# 依次执行，很明显


# 我们用多线程来试试
# import threading
# from time import ctime, sleep

# def _music1(musicName):
# 	print('我在听{},时间: {}'.format(musicName, ctime()))
# 	sleep(2)

# def _movies(movieName):
# 	print('我在看{},时间: {}'.format(movieName, ctime()))
# 	sleep(4)

# def main1():
# 	threads = []
# 	# 创建线程
#   # 语法:class threading.Thread(group=None, target=None, name=None, args=(), kwargs={})
# 	t1 = threading.Thread(target=_music1, args=('老子明天不上班',))
# 	t2 = threading.Thread(target=_movies, args=('战狼2',))
# 	threads.append(t1)
# 	threads.append(t2)

# 	for t in threads:
# 		# 守护线程 必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起
# 		# 设置守护线程就是说这个线程不重要，主程序要退出不需要等待它执行完成。
# 		# 否则，需要所有的非守护线程执行完了才可以退出
# 		t.setDaemon(True) 
# 		t.start()

# 	print('all over {}'.format(ctime()))


# if __name__ == '__main__':
# 	main1()
# 我在听老子明天不上班,时间: Tue Sep  5 20:36:48 2017
# 我在看战狼2,时间: Tue Sep  5 20:36:48 2017
# all over Tue Sep  5 20:36:48 2017
# 看看时间就知道了，是同时执行的。


# 再试试 join() 方法
# import threading
# from time import ctime, sleep

# def _music1(musicName):
# 	print('我在听{},时间: {}'.format(musicName, ctime()))
# 	sleep(2)

# def _movies(movieName):
# 	print('我在看{},时间: {}'.format(movieName, ctime()))
# 	sleep(4)

# def main1():
# 	threads = []
# 	# 创建线程
# 	t1 = threading.Thread(target=_music1, args=('老子明天不上班',))
# 	t2 = threading.Thread(target=_movies, args=('战狼2',))
# 	threads.append(t1)
# 	threads.append(t2)

# 	for t in threads:
# 		# 守护线程 必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起
# 		# 设置守护线程就是说这个线程不重要，主程序要退出不需要等待它执行完成。
# 		# 否则，需要所有的非守护线程执行完了才可以退出
# 		t.setDaemon(True) 
# 		t.start()

# 	t.join()

# 	print('all over {}'.format(ctime()))


# if __name__ == '__main__':
# 	main1()

# 我在听老子明天不上班,时间: Tue Sep  5 20:41:53 2017
# 我在看战狼2,时间: Tue Sep  5 20:41:53 2017
# all over Tue Sep  5 20:41:57 2017
# 神奇吧， 注意 t.join()位置在for循环外，
# join（）在这里的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
# 假如有两个线程 A B,在A中使用join()意味着A执行完成后才能执行B。


# 上面的案例都是用的threading.Thread()方法创建线程。
# 实际项目中常用到的是通过类继承实现
# import threading
# from time import ctime, sleep

# class myThread (threading.Thread):

# 	def __init__(self, threadName, delay):
# 		threading.Thread.__init__(self)
# 		self.threadName = threadName
# 		self.delay = delay

# 	def run(self):
# 		print('{} is start at {}'.format(self.threadName, ctime()))
# 		delay_time(threadName=self.threadName, delay=self.delay)

# def delay_time(delay, threadName):
# 	print('{} at {}'.format(threadName, ctime()))
# 	sleep(delay)

# if __name__ == '__main__':
# 	thread1 = myThread('线程1', 2)
# 	thread2 = myThread('线程2', 4)
# 	threads = []
# 	threads.append(thread1)
# 	threads.append(thread2)
# 	for t in threads:
# 		t.setDaemon(True)
# 		t.start()
# 		t.join()
# 	print('over at {}'.format(ctime()))



## 同步锁机制
# class myThread (threading.Thread):

# 	def __init__(self, threadName, delay):
# 		threading.Thread.__init__(self)
# 		self.threadName = threadName
# 		self.delay = delay

# 	def run(self):
# 		print('{} is start at {}'.format(self.threadName, ctime()))
# 		threadLock.acquire() # 上锁
# 		print('{}上锁'.format(self.threadName))
# 		delay_time(threadName=self.threadName, delay=self.delay)
# 		threadLock.release() # 释放锁
# 		print('{}释放锁'.format(self.threadName))

# def delay_time(delay, threadName):
# 	print('{} at {}'.format(threadName, ctime()))
# 	sleep(delay)

# if __name__ == '__main__':
# 	# 使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步
# 	threadLock = threading.Lock()

# 	thread1 = myThread('线程1', 3)
# 	thread2 = myThread('线程2', 5)

# 	thread1.start()
# 	thread2.start()

# 	threads = []
# 	threads.append(thread1)
# 	threads.append(thread2)

# 	# 等待所有线程完成
# 	for t in threads:
# 		t.join()
		
# 	print('over at {}'.format(ctime()))
# 线程1 is start at Tue Sep  5 21:26:38 2017
# 线程1上锁
# 线程1 at Tue Sep  5 21:26:38 2017
# 线程2 is start at Tue Sep  5 21:26:38 2017
# 线程1释放锁
# 线程2上锁
# 线程2 at Tue Sep  5 21:26:41 2017
# 线程2释放锁
# over at Tue Sep  5 21:26:46 2017



# # Queue

# ## 一个简单的Queue与多线程
# import queue
# import threading
# from time import ctime, sleep

# q = queue.Queue(10)
# MAX_THREAD_NUM = 3 # 线程数

# class myThread(threading.Thread):

# 	def __init__(self, func):
# 		threading.Thread.__init__(self)
# 		self.func = func

# 	def run(self):
# 		self.func()

# def worker():
# 	global q
# 	while not q.empty():
# 		item = q.get() #获取任务
# 		print('Processing : {}'.format(item))
# 		sleep(1)
# def main():
# 	global q
# 	threads = []

# 	for i in range(5): #向队列填充任务
# 		q.put(i)

# 	for j in range(MAX_THREAD_NUM):
# 		thread = myThread(worker)
# 		thread.start()
# 		threads.append(thread)

# 	for o in threads:
# 		o.join()
# 	print('all over')
# if __name__ == '__main__':
# 	main()

# # Processing : 0
# # Processing : 1
# # Processing : 2
# # Processing : 3
# # Processing : 4
# # all over




# demo: 用三个线程输出 one two three four five
# import queue
# import threading
# from time import ctime, sleep

# # 定义一个开关
# flag = 0

# # 线程类，重写run方法
# class myThread(threading.Thread):

# 	def __init__(self, id, name, q):
# 		threading.Thread.__init__(self)
# 		self.id = id
# 		self.name = name
# 		self.q = q

# 	def run(self):
# 		print('启动线程{}'.format(self.name))
# 		print_s(self.name, self.q)
# 		print('退出线程{}'.format(self.name))

# # 打印方法
# def print_s(name, q):
# 	while not myQueue.empty():
# 		print('{} process {}'.format(name, q.get()))
# 		sleep(2)

# threadNameList = ['线程1', '线程2', '线程3']
# numQueue = ['one', 'two', 'three', 'four', 'five']

# # 同步锁
# queueLock = threading.Lock()
# # 队列
# myQueue = queue.Queue(10)

# threadId = 1
# threads = []

# # 队列填充数据
# #queueLock.acquire()
# for i in numQueue:
# 	myQueue.put(i)
# #queueLock.release()


# # 创建线程
# for t in threadNameList:
# 	_t = myThread(threadId, t, myQueue)
# 	_t.start()
# 	threads.append(_t)
# 	threadId += 1



# # # 等待队列清空
# # while not myQueue.empty():
# #     pass

# flag = 1

# for j in threads:
# 	j.join()



# threadlocal
import threading

# 创建一个local
local_student = threading.local()

def proce():
	std = local_student.student
	print('hello,{}-->in thread {}'.format(std, threading.current_thread().name))

def make_local(name):
	local_student.student = name
	proce()

if __name__ == '__main__':
	t1 = threading.Thread(target= make_local, args=('Alice',), name='Thread-A')
	t2 = threading.Thread(target= make_local, args=('Bob',), name='Thread-B')

	t1.start()
	t2.start()

	t1.join()
	t2.join()
# hello,Alice-->in thread Thread-A
# hello,Bob-->in thread Thread-B