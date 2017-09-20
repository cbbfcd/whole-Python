# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-09-20 21:24:35
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-20 22:50:10


# 多进程

# 1. multiprocessing模块
# from multiprocessing import Process
# import os

# # 子程序执行的方法
# def run_in_child(name):
# 	print('子程序名称{},ID是{}'.format(name, os.getpid()))
# 	print('父进程ID是{}'.format(os.getppid()))

# def main_process():
# 	print('父进程ID{}是'.format(os.getpid()))
# 	p = Process(target=run_in_child, args=('child_process',))# 创建子进程实例
# 	print('启动子进程')
# 	p.start() # 启动进程
# 	p.join()  # 同步等待结束之后执行
# 	print('子进程结束')
# if __name__ == '__main__':
# 	main_process()

# 父进程ID552是
# 启动子进程
# 子程序名称child_process,ID是8476
# 父进程ID是552
# 子进程结束



# 2. 进程池
# from multiprocessing import Pool
# import os, time, random

# def run_in_child(name):
# 	print('子程序{},ID是{}'.format(name, os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random() * 5)
# 	end = time.time()
# 	print('子进程{}运行了{:.2}s'.format(name, end-start))

# def main_process():
# 	print('父进程ID{}'.format(os.getpid()))
# 	p = Pool(4) # 创建容量为4的进程池
# 	for i in range(0,5):
# 		p.apply_async(run_in_child, args=(i,))
# 	p.close()
# 	p.join()
# 	print('所有进程都结束了')
# if __name__ == '__main__':
# 	main_process()

# 父进程ID11084
# 子程序1,ID是15556
# 子进程1运行了3.0s
# 子程序0,ID是1288
# 子进程0运行了4.2s
# 子程序3,ID是12556
# 子进程3运行了4.6s
# 子程序2,ID是13560
# 子进程2运行了2.1s
# 子程序4,ID是13560
# 子进程4运行了4.9s
# 所有进程都结束了




# 3. 进程之间的通信
# from multiprocessing import Process, Queue
# import os, time, random

# # 往queue中写入数据
# def write_in_queue(q):
# 	print('进程{}开始写入数据'.format(os.getpid()))
# 	i='test'
# 	print('写入{}'.format(i))
# 	q.put(i)
# 	time.sleep(random.random())


# # 往queue中读取数据
# def read_from_queue(q):
# 	print('进程{}开始读取数据'.format(os.getpid()))
# 	_q = q.get()
# 	print('读取到数据{}'.format(_q))

# def main_process():
# 	print('父进程{}'.format(os.getpid()))
# 	q = Queue()

# 	pw = Process(target=write_in_queue, args=(q,))
# 	pr = Process(target=read_from_queue, args=(q,))

# 	# 启动子进程
# 	pw.start()
# 	pr.start()

# 	# 等待写完
# 	pw.join()
# 	pr.join()

# 	# 强行结束
# 	pr.terminate()


# if __name__ == '__main__':
# 	main_process()

# 父进程12872
# 进程17680开始读取数据
# 读取到数据test
# 进程20208开始写入数据
# 写入test





# pipe
import multiprocessing
import time

def proc1(pipe):
	i = 'hello world'
	pipe.send(i)
	print('接收到{}'.format(pipe.recv()))
	time.sleep(1)

def proc2(pipe):
	print('接收{}'.format(pipe.recv()))
	pipe.send('hello too!')
	time.sleep(1)

if __name__ == '__main__':
	print('主线程')
	pipe = multiprocessing.Pipe()
	p1 = multiprocessing.Process(target=proc1, args=(pipe[0],))
	p2 = multiprocessing.Process(target=proc2, args=(pipe[1],))

	p1.start()
	p2.start()

	p1.join()
	p2.join()