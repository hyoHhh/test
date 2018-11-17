# -*- coding: utf-8 -*-
import re
import urllib2
import selenium
import selenium.webdriver
# user_input=input("请出入您需要爬取的内容")
# 网页屏蔽 模拟浏览器
def download1(url):
    return urllib2.urlopen(url).read()

# url  = 'https://sou.zhaopin.com/?jl=530&kw=java&kt=3'
# print download1(url)


# 考虑空白元素
def getnumberbyname(searchname):
    url = 'https://sou.zhaopin.com/?jl=530&kw={}&kt=3'.format(searchname)
    driver = selenium.webdriver.Firefox()
    driver.get(url)
    pagesource = driver.page_source
    driver.close()
    return pagesource
print(getnumberbyname("python"))

# urlopen(url,data=none,timeout)
