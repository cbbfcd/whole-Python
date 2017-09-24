# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-09-21 23:27:10
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-23 23:35:48


# 协程

# 简单创建一个协程
import time
import asyncio
import functools
# now = lambda : time.time()

# ## 定义一个简单的协程
# async def do_some(x):
# 	print('等待：{}'.format(x))

# start = now()

# ## 协程不能单独的执行，需要放进事件循环
# coroutine = do_some(2)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)

# print('TIME :', now() - start)
# 等待：2
# TIME : 0.015625715255737305


## Task
# now = lambda : time.time()

# async def do_some(x):
# 	print('等待：{}'.format(x))

# start = now()

# ## 协程不能单独的执行，需要放进事件循环
# coroutine = do_some(2)
# ## 事件池子
# loop = asyncio.get_event_loop()
# ## --> 创建一个task
# task = loop.create_task(coroutine)
# print(task)
# loop.run_until_complete(task)
# print(task)
# print('TIME :', now() - start)
# <Task pending coro=<do_some() running at E:\Python\PythonNotes\python基础\code\chapter21.py:36>>
# 等待：2
# <Task finished coro=<do_some() done, defined at E:\Python\PythonNotes\python基础\code\chapter21.py:36> result=None>
# TIME : 0.0005006790161132812




# 绑定回调

# now = lambda: time.time()
# # 协程函数
# async def do_some(x):
# 	print('等待：{}'.format(x))
# 	return '这是返回值{}'.format(x)

# # 回调函数
# def callback(arg1,arg2,future):
# 	print('callback: {} and arg1:{},arg2:{}'.format(future.result(), arg1, arg2))

# start = now()
# # 事件循环
# loop = asyncio.get_event_loop()

# # 封装task
# task = loop.create_task(do_some(2))

# # 绑定回调
# # task.add_done_callback(functools.partial(callback, 'hello', 'world'))

# # 注册到事件循环并启动事件循环
# loop.run_until_complete(task)
# print('TIME: ', now() - start)
# print('不绑定回调，输出结果{}'.format(task.result()))

# # 等待：2
# # TIME:  0.0
# # 不绑定回调，输出结果这是返回值2

# # 等待：2
# # callback: 这是返回值2 and arg1:hello,arg2:world
# # TIME:  0.0014820098876953125




# await
# now = lambda : time.time()

# 模拟耗时协程
# async def some_func():
# 	await asyncio.sleep(2)
# 	return '耗时操作结束'

# # 另一个协程，当耗时协程挂起的时候，事件循环就会执行别的协程，
# # 当其他协程也挂起或者结束的时候再执行下一个。
# async def another_func():
# 	return '这是另一个协程'

# start = now()
# # 事件循环
# loop = asyncio.get_event_loop()

# # 创建task
# task1 = loop.create_task(some_func())
# task2 = loop.create_task(another_func())

# # 注册到事件循环，并启动
# loop.run_until_complete(task1)
# loop.run_until_complete(task2)
# print(task1.result(),task2.result())
# print('TIME: ', now() - start)



# 并发

# 1. 同步的情况
# now = lambda : time.time()

# async def do_some(x):
# 	print('协程{}'.format(x))
# 	time.sleep(x)
# 	return '协程{}执行完毕'.format(x)

# start = now()

# tasks = [
# 	asyncio.ensure_future(do_some(1)),
# 	asyncio.ensure_future(do_some(2)),
# 	asyncio.ensure_future(do_some(4))
# ]

# loop = asyncio.get_event_loop()

# # asyncio.gather(*tasks) 接受一堆task
# # asyncio.wait(tasks) 接受一个列表
# loop.run_until_complete(asyncio.wait(tasks))

# for task in tasks:
# 	print(task.result())

# print('TIME: ', now() - start)

# 协程1
# 协程2
# 协程4
# 协程1执行完毕
# 协程2执行完毕
# 协程4执行完毕
# TIME:  7.031957149505615

# # 2.　并发的情况
# now = lambda : time.time()

# async def do_some(x):
# 	print('协程{}'.format(x))
# 	await asyncio.sleep(x)
# 	return '协程{}执行完毕'.format(x)

# start = now()

# tasks = [
# 	asyncio.ensure_future(do_some(1)),
# 	asyncio.ensure_future(do_some(2)),
# 	asyncio.ensure_future(do_some(4))
# ]

# loop = asyncio.get_event_loop()

# # asyncio.gather(*tasks) 接受一堆task
# # asyncio.wait(tasks) 接受一个列表
# loop.run_until_complete(asyncio.wait(tasks))

# for task in tasks:
# 	print(task.result())
# print('TIME: ', now() - start)

# # 协程1
# # 协程2
# # 协程4
# # 协程1执行完毕
# # 协程2执行完毕
# # 协程4执行完毕
# # TIME:  4.015275716781616


# 协程嵌套

# now = lambda : time.time()

# # 任务协程
# async def do_some(x):
# 	print('协程{}'.format(x))
# 	await asyncio.sleep(x)
# 	return '协程{}执行完毕'.format(x)

# # 主协程
# async def main():
# 	tasks = [
# 		asyncio.ensure_future(do_some(1)),
# 		asyncio.ensure_future(do_some(2)),
# 		asyncio.ensure_future(do_some(4))
# 	]

# 	dones, pendings = await asyncio.wait(tasks)

# 	for task in dones:
# 		print(task.result())

# 	return 'main协程执行完毕'
# start = now()

# loop = asyncio.get_event_loop()
# main_task = loop.create_task(main())
# loop.run_until_complete(main_task)
# print(main_task.result())
# print('TIME: ', now() - start)

# 协程1
# 协程2
# 协程4
# 协程4执行完毕
# 协程1执行完毕
# 协程2执行完毕
# main协程执行完毕
# TIME:  4.014368295669556


# now = lambda : time.time()

# # 任务协程
# async def do_some(x):
# 	print('协程{}'.format(x))
# 	await asyncio.sleep(x)
# 	return '协程{}执行完毕'.format(x)

# # 主协程
# async def main():
# 	tasks = [
# 		asyncio.ensure_future(do_some(1)),
# 		asyncio.ensure_future(do_some(2)),
# 		asyncio.ensure_future(do_some(4))
# 	]

# 	return await asyncio.wait(tasks)
# start = now()
# loop = asyncio.get_event_loop()
# main_task = loop.create_task(main())
# dones, pendings = loop.run_until_complete(main_task)
# for i in dones:
# 	print(i.result())
# print('TIME: ', now() - start)


# 停止
# now = lambda : time.time()
# # 任务协程
# async def do_some(x):
# 	print('协程{}'.format(x))
# 	await asyncio.sleep(x)
# 	return '协程{}执行完毕'.format(x)

# # 主协程
# async def main():
# 	tasks = [
# 		asyncio.ensure_future(do_some(1)),
# 		asyncio.ensure_future(do_some(2)),
# 		asyncio.ensure_future(do_some(4))
# 	]
# 	a = 1/0
# 	dones, pendings = await asyncio.wait(tasks)

# 	for task in dones:
# 		print(task.result())
# start = now()
# loop = asyncio.get_event_loop()
# main_task = loop.create_task(main())
# try:
# 	loop.run_until_complete(main_task)
# except ZeroDivisionError  as e:
# 	print(asyncio.Task.all_tasks())
# 	print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())
# 	loop.stop()
# 	loop.run_forever()
# finally:
# 	loop.close()
# print('TIME: ', now() - start)


# 7. 多线程中的事件循环
# from threading import Thread
# now = lambda : time.time()
# # 开启事件循环
# def start_loop(loop):
# 	asyncio.set_event_loop(loop)
# 	loop.run_forever()

# # more jobs
# def more_jobs(x):
# 	print('more jobs {}'.format(x))
# 	time.sleep(x)
# 	print('more jobs {} is over'.format(x))

# start = now()

# # 在主线程创建一个事件循环。
# new_loop = asyncio.new_event_loop()

# # 创建一个新的线程
# t = Thread(target=start_loop , args=(new_loop,))
# t.start()
# print('TIME: {}'.format(time.time() - start))

# new_loop.call_soon_threadsafe(more_jobs, 6)
# new_loop.call_soon_threadsafe(more_jobs, 3)


# more jobs 6
# more jobs 6 is over
# more jobs 3
# more jobs 3 is over


# 并发的多线程和协程模型

from threading import Thread
now = lambda : time.time()
# 动态建立并开启事件循环
# def start_loop(loop):
# 	asyncio.set_event_loop(loop)
# 	loop.run_forever()

# # more jobs
# async def more_jobs(x):
# 	print('more jobs {}'.format(x))
# 	await asyncio.sleep(x)
# 	print('more jobs {} is over'.format(x))

# start = now()

# # 在主线程创建一个事件循环。
# new_loop = asyncio.new_event_loop()

# # 创建一个新的线程
# t = Thread(target=start_loop , args=(new_loop,))
# t.start()
# print('TIME: {}'.format(time.time() - start))

# asyncio.run_coroutine_threadsafe(more_jobs(6), new_loop)
# asyncio.run_coroutine_threadsafe(more_jobs(3), new_loop)

# more jobs 6
# more jobs 3
# more jobs 3 is over
# more jobs 6 is over