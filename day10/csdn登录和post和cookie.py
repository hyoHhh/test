# -*- coding: utf-8 -*-
import urllib,urllib2,re,cookielib
#建立cookie管理器，用这个打开自带cookie

url  =  'https://passport.csdn.net/'
cookie = cookielib.CookieJar()

cookieproc=urllib2.HTTPCookieProcessor(cookie)

opener=urllib2.build_opener(cookieproc)

html=opener.open(url).read().decode("utf-8")
print(html)
