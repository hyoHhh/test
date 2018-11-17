# -*- coding: utf-8 -*-
import threading
import Queue
import urllib2
import time

def getdata(url):
    try:
        data=urllib2.urlopen(url).read().decode('utf-8')
        return data

    except:
        return "异常"
url = 'https://bbs.tianya.cn/m/post-140-393974-6.shtml'


import re
def getemail(data):
    try:
        mailregex=re.compile (r"([0-9a-zA-Z.%+\-]+@[0-9a-zA-Z.\-]+\.[A-Za-z]{1,3})",re.IGNORECASE)
        mylist = mailregex.findall(data)
        return mylist

    except:
        return []
data=getdata(url)
time.sleep(5)
test='lingdianbing@sina.com'
data=getdata(url)
kk=getemail(data)
print(kk)