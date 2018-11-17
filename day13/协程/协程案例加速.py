# -*- coding: utf-8 -*-
import gevent
import time
def showwait(name,n):
    for i in range(n):
        print(name,"等待了",i+1,"秒")
        # 加速
        # 切换任务
        # gevent.sleep(1)  #不需要等待就顺序执行，需要等待就自动切换，
        # time.sleep()不会自动切换

g1=gevent.spawn(showwait,'李乐靖',10)
g2=gevent.spawn(showwait,'肖雯文',10)
g3=gevent.spawn(showwait,'鼠来宝',10)
g1.join()
g2.join()
g3.join()