# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import urllib2
import cookielib

filepath = 'cookies.txt'

cookie = cookielib.LWPCookieJar(filepath)  # 设置cookie保存文件和路径

header = urllib2.HTTPCookieProcessor(cookie)  #设置cookie头，与网站有关

opener = urllib2.build_opener(header)

response = opener.open("http://www.baidu.com")

cookie.save(ignore_discard=True,ignore_expires=True) #忽略