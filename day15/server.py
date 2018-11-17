# -*- coding: utf-8 -*-
import multiprocessing  #分布式进程

import multiprocessing.managers  #分布式进程管理器

import random,time  #随机数和书剑

import Queue

task_queue =Queue.Queue()  #任务
result_queue = Queue.Queue()  #结果

def return_task():
    return task_queue

def return_result():
    return result_queue


class QueueManger(multiprocessing.managers.BaseManager): #继承，进程管理共享数据
    pass


if __name__ == '__main__':
    multiprocessing.freeze_support()  #开启分布式支持

    QueueManger.register('get_task',callable=return_task) #注册函数给客户端用
    QueueManger.register('get_result',callable=return_result)

    manger =QueueManger(address=("192.168.0.100",8848),authkey="hyolyn")#创建管理器设置密码
    manger.start()
    task=manger.get_task()
    result=manger.get_result()
    for i in range(10000):
        print("task add data",i)
        task.put(i)

    print("waittingfor ----")
    for i in range(10000):
        res = result.get()
        print("get data ",res)

    manger.shutdown()#关闭服务器

