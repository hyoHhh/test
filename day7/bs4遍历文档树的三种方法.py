# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
# 缺点，速度慢 beautifulsoup的缺点
import re

from bs4 import BeautifulSoup

html="""

<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>title</title>
</head>
<body>
<p class="title" name="dromouse"><b>The dormouse`s story</b></p>
<a href="h2.html" class="brother" id="link2">
    日历
</a>
<a href="h1.html" class="sister" id="link3">
    天气
</a>

</body>

</html>
"""
#
#

soup=BeautifulSoup(html,'lxml')  #lxml代表一种解析方式
soup1=BeautifulSoup(html,'html.parser')  #常规网页解析
soup2=BeautifulSoup(html,'html5lib')   #HTML5解析

# for child in soup.body.children:
    # print(child.string)

# print(soup.find_all('a'))
# print(soup.find_all('a')[0].attrs['class'][0]) #找所有
print(soup.find_all(["a",'p'])[0].attrs['class'][0]) #找所有
print(soup.find_all(id='link2')) #找所有
print(soup.find_all(text=['1','2','3'])) #满足一个就可以了
print(soup.find_all(id=re.compile('Dormouse'))) #正则表达式
# print(soup.find())#找第一个

a_tag=soup.select('a')#找所有  #CSS选择器
