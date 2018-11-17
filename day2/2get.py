# -*- coding: utf-8 -*-
import urllib2
import urllib

word = {'wd':"李乐靖"}

url = "http://www.baidu.com/s"
word  = urllib.urlencode(word)  #编码成字符串
newurl = url+"?" + word  # 拼接网址

request = urllib2.Request(newurl)  # 发起请求
print(urllib2.urlopen(request).read()) #读取看信息