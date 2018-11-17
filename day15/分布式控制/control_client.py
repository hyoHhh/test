# -*- coding: utf-8 -*-
# 批量关机,批量开机
# 发送命令调用os 执行命令

import multiprocessing  #分布式进程

import multiprocessing.managers  #分布式进程管理器

import random,time  #随机数和书剑

import Queue

import os

class QueueManger(multiprocessing.managers.BaseManager): #继承，进程管理共享数据


    pass

if __name__ == '__main__':
    QueueManger.register("get_task")
    QueueManger.register("get_result")
    manger =QueueManger(address=("192.168.0.100",8848),authkey="hyolyn")#创建管理器设置密码
    manger.connect()  #连接服务器
    task=manger.get_task()
    result=manger.get_result()
    for i in range(10):
        try:
            data=task.get()
            print("client get",data)
            code=os.system(data)
            # result.put('client'+str(data+10))
            result.put('client'+code)
        except Exception as e:
            pass

