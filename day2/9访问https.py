# -*- coding: utf-8 -*-
import urllib2

import urlparse

import ssl

# def download1(url):
    # return urllib2.urlopen(url).read()


context = ssl._create_unverified_context()#忽略安全

url = "https://www.baidu.com"

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

request=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(request,context=context)
print(response.read())