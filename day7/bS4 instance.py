# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
def download(url):
    headers = {'User-agent':"None"}
    req=urllib.request.Request(url,headers=headers)
    data=urllib.request.urlopen(req)
    data=data.read()
    soup=BeautifulSoup(data,"lxml",from_encoding="utf-8")
    spanlist=soup.find_all("span",class_='search_yx_tj')
    print(spanlist)

url = 'http://sou.zhaopin.com/'
download(url)

