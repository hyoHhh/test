# -*- coding: utf-8 -*-

import threading

import time
def myThread(name):
    with sep:
        for i in range(19):
            time.sleep(1)

            print name,str(i),threading.current_thread().name

sep = threading.Semaphore(1)  #限制条件，只允许一个url运行
threadlist=[]
for name in ['a','b','c','d','e']:
    mythd=threading.Thread(target=myThread,args=(name,))
    mythd.start()
    threadlist.append(mythd)


for thred in threadlist:
    thred.join()