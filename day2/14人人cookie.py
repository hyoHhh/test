# -*- coding: utf-8 -*-
import urllib2
import urllib
import cookielib
# 创建一个储存对象储存cookie
cookie = cookielib.CookieJar()

#创建一个链接对象使用cookie
cookie_hander = urllib2.HTTPCookieProcessor(cookie)

# 打开器，使用cookie
opener= urllib2.build_opener(cookie_hander)
#增加一个浏览器模拟
opener.addheaders[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')]

loginurl = "http://www.renren.com/PLogin.do"

data = {"email":"yincheng5201314@163.com","password":"tsinghua"}

data = urllib.urlencode(data) #编码

request = urllib2.Request(loginurl,data=data)#post请求登陆,抓取cookie

response = opener.open(request) #载入cookie

response_index = opener.open("http://www.renren.com/24224565/profile")

print(response_index.read())