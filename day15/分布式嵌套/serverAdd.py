# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
# 批量关机,批量开机

import multiprocessing  # 分布式进程

import multiprocessing.managers  # 分布式进程管理器

import os

import random, time  # 随机数和书剑

import Queue

task_queue = Queue.Queue()  # 任务
result_queue = Queue.Queue()  # 结果


def return_task():
    return task_queue


def return_result():
    return result_queue


class QueueManger(multiprocessing.managers.BaseManager):  # 继承，进程管理共享数据
    pass


if __name__ == '__main__':
    os.system("notepad")
    multiprocessing.freeze_support()  # 开启分布式支持

    QueueManger.register('get_task', callable=return_task)  # 注册函数给客户端用
    QueueManger.register('get_result', callable=return_result)

    manger = QueueManger(address=("192.168.0.100", 8868),
                         authkey="hyolyn")  # 创建管理器设置密码
    manger.start()
    task = manger.get_task()
    result = manger.get_result()
    for i in range(100):
        print("task add data",i)
        task.put("来自远古的"+str(i))

    print("waittingfor ----")
    savefile = open("mind.txt","wb") #结果写入文本
    for i in range(100):
        res = result.get(timeout=100)
        savefile.write(res)
        print("get data ", res)
        savefile.flush()
    savefile.close()
    manger.shutdown()  # 关闭服务器