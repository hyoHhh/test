# -*- coding: utf-8 -*-

import requests

response=requests.get("http://www.baidu.com")
print(response.text)  #网页文本
print(response.status_code)#状态
print(response.headers)#请求头
print(response.cookies)  #cookie
print(response.content) # 网页内容
print(response.url)  #链接
print(response.history)  #链接
print(response.is_redirect)  #是否重定向
print(response.encoding)  #编码
print(response.links)  #子链接

#---------------  分割线--------------------get协议

#
# data = {"wd":"李乐靖"}
#
# headers={""}
#
# url ="baidu"
#
# req=requests.get(url,headers=headers)



#---------------  分割线--------------------post协议

# requests.post(url,params=data,headers=headers)



#---------------  分割线--------------------证书


# req = requests.get("https://www.12306.cn",verify=True)
#
# print(req)

import json

req = requests.get("http://www.baidu.com",verify=False) #默认用证书，可以设置成年false

print(req)



#---------------  分割线--------------------cookie简单实用

mycookie=dict(BDSID="zhadu")

req=requests.get("http://www.baidu.com",cookies=mycookie)

print(req.cookies)
print(req.text)


#---------------  分割线--------------------session登录

mysession=requests.session()
dicin={"1":"1"}
mysession.post('http://www.baidu.com',cookies=dicin)
mysession.cookies.get__dict()


#---------------  分割线--------------------利用selenium和requests
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
cookies=driver.get_cookies()
req=requests.Session()
for cook in cookies:
    req.cookies.set(cook["name"],cook['value'])


req.headers.clear() #请空头

newpage=req.get("")


