# -*- coding: utf-8 -*-
# 缺点，速度慢 beautifulsoup的缺点
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

</body>
<p class="title" name="dromouse"><b>The dormouse`s story</b></p>
<a href="h2.html" class="brother" id="link2">
    日历
</a>
<a href="h1.html" class="sister" id="link3">
    天气
</a>

</html>
"""
#
#

soup=BeautifulSoup(html,'lxml')  #lxml代表一种解析方式
soup1=BeautifulSoup(html,'html.parser')  #常规网页解析
soup2=BeautifulSoup(html,'html5lib')   #HTML5解析
# print(soup.prettify())
# print(soup1.prettify())
# print(soup2.prettify())
# print(type(soup))
print(soup.a) #提取标签的全部内容
print(soup.title.string) #取出标签中间的文本比如P标签或者a标签中间的文字
print(soup.a.attrs['href'])
print(soup.a.attrs)  #{'href': 'h2.html', 'class': ['brother'], 'id': 'link2'}
a=soup.select('a')
print(a)
for i in a:
    print(i.attrs)
