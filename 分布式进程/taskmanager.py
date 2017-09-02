#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 创建两个队列作为交换对象,分别存放任务和结果,用于进行进程间的通信
task_queue = queue.Queue()
result_queue = queue.Queue() 

class QueueManager(BaseManager):
    pass

def task_q():
    return task_queue

def result_q():
    return result_queue

def server_start():
	# 将两个队列注册到网络上
    QueueManager.register('get_task_queue', callable=task_q)
    QueueManager.register('get_result_queue', callable=result_q)
    # 创建对象,绑定端口6000,设置验证码'abc'
    manager = QueueManager(address=('127.0.0.1', 6000), authkey=b'abc')
    # 启动管理
    manager.start()
    # 获取通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 往task队列放任务
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列取结果
    print('Try getting result')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)
    # 关闭管理
    manager.shutdown()
    print('master exit.')    

if __name__ == '__main__':
    freeze_support() 
    server_start()