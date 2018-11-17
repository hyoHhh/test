# -*- coding: utf-8 -*-
import greenlet
import time
def go1():
    print("我是李乐靖，雪糕我先吃一口")  #1
    gr2.switch()
    time.sleep(1)

def go2():
    print("我是雯文，雪糕我先吃一口")   #2
    gr1.switch()
    time.sleep(1)


if __name__ == '__main__':

    gr1=greenlet.greeenlet(go1)
    gr2=greenlet.greeenlet(go2)
    gr1.switch()