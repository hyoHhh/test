# -*- coding: utf-8 -*-

from multiprocessing import Pool
import time
import os

def getdata(data):
    print os.getpid(),"start"

    print os.getpid(),"end"

    return data*data
a=time.time()

if __name__ == '__main__':

    mylist=[x for x in range(2000000)]
    pool=Pool(processes=5)

    pool_output=pool.map(getdata,mylist)  #抓取进程池的所有结果

    pool.close()
    pool.join()

    print(pool_output)

    b=time.time()
#
    print(b-a)
# a=time.time()
# datalist=[]
# for i in range(2000000):
#     z=getdata(i)
#     datalist.append(z)
#
# print(datalist)
#
# b=time.time()
# print(b-a)