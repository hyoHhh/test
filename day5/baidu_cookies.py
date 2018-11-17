# -*- coding: utf-8 -*-
#主页，用户编号，登录，三个页面
import cookielib
import urllib2
import urllib
url_index = 'http://www.baidu.com'

url_baidu_token = "https://passport.baidu.com/v2/api/?getapi&tpl=pp&apiver=v3&class=login"

url_login = 'https://passport.baidu.com/v2/api/?login'

user = "fjlha848"

password = "hyolyn11.14"

cookiejar = cookielib.CookieJar() #cookie管理器

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar)) #打开按照这个cookie管理器

urllib2.install_opener(opener)  #全局生效

# reqReturn = urllib2.urlopen(url_index) #打开主页

#抓取token
import re
tokenReturn = urllib2.urlopen(url_baidu_token)
print(tokenReturn.read())
n = re.search(u'"token":"(?P<tokenVal>.*?)"',tokenReturn.read())
tokenVal=n.group("tokenVal")
print(tokenVal)

# post 登录

postData = {
    "username":user,
    "password":password,
    'u':'https://passport.baidu.com/',
    'tpl':'pp',
    'token':tokenVal,
    'staticpage':'https://passport.baidu.com/static/passpc-account/html/v3Jump.html',
    'isPhone':'false',
    'charset':'utf-8',
    'callback':'parent.bd__pcbs__ra48vi',
}
postData=urllib.urlencode(postData)  #编码转换


loginRequest  = urllib2.Request(url_login,postData) #模拟登录
loginRequest.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
loginRequest.add_header('Accept-Encoding','gzip, deflate, br')
loginRequest.add_header('Accept-Language','zh-CN,zh;q=0.9')
loginRequest.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
loginRequest.add_header('Content-Type','application/x-www-form-urlencoded')

sendPost = urllib2.urlopen(loginRequest)