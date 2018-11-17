# -*- coding: utf-8 -*-
from multiprocessing import Pool
from multiprocessing import Barrier
from multiprocessing import Process
import os
import time
import multiprocessing

def getdata(data,myBarrier):
    with myBarrier:
        print (os.getpid(),'start')
        time.sleep(3)
        print (os.getpid(),'end',data*data)

if __name__ == '__main__':
    myBarrier=Barrier(3)

    mylist=[x for x in range(100)]

    processlist=[]

    for data in mylist:
        process=Process(target=getdata,args=(data,myBarrier))
        processlist.append(process)
        process.start()
    for process in processlist:
        process.join()
