# -*- coding: utf-8 -*-
import urllib2
import cookielib

cookie = cookielib.CookieJar()
header = urllib2.HTTPCookieProcessor(cookie)

opener=urllib2.build_opener(header)

response = opener.open("http://www.baidu.com/")

cookies = ""
for data in cookie:
    cookies=cookies+data.name+"="+data.value+":\r\n"

print(cookies)