# -*- coding: utf-8 -*-
import pyquery

# xpath beautifulsoup re lxml 解析库  pyquery

url = 'http://www.baidu.com'

# import requests
#
# response=requests.get(url)
#
# print(response.encoding)
# text=response.text.decode('ISO-8859-1').encode("utf-8")
# pyq=pyquery.PyQuery(text)
# print(pyq("title"))
import lxml.etree

doc3 = pyquery.PyQuery('http://www.baidu.com')
print(doc3)


# ----------------分割-------------pyquery初始化的四种风格
doc1 = pyquery.PyQuery("<html></html>")
doc2 = pyquery.PyQuery(lxml.etree.fromstring('<html></html>'))
doc3 = pyquery.PyQuery('http://www.baidu.com',headers={"1","1"})
doc4 = pyquery.PyQuery(filename="index.html")