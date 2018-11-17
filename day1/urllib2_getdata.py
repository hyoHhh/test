# -*- coding: utf-8 -*-
import urllib2
def download1(url):
    return urllib2.urlopen(url).read()

# urllib2 只能处理http，不能处理https
url = "http://www.baidu.com/"
# print(download1(url))  读取全部网页

def download2(url):
    return urllib2.urlopen(url).readlines()  #读取每行网页，压入到列表

print(download2(url))

def download3(url):
    reponse = urllib2.urlopen(url)
    while True:
        line=reponse.readline()
        if not line:
            break
        print(line)
print download3(url)

url2 = 'http://www.zhaopin.com/'
