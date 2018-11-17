# -*- coding: utf-8 -*-
import jsonpath
import urllib2
import json
import chardet
url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"

jsonstr=urllib2.urlopen(url).read()  # 抓取网页的json数据
jsontree=json.loads(jsonstr)   #转化为json对象
print(jsonpath.jsonpath(jsontree,"$..name"))
mylist=jsonpath.jsonpath(jsontree,"$..name")
mylist=jsonpath.jsonpath(jsontree,"$..id")
mylist=jsonpath.jsonpath(jsontree,"$..code")
mylist=jsonpath.jsonpath(jsontree,"$.content")
for line in mylist:
    print(line)

compare="""
n/a表示不支持
    /       $
    .       @
    /       . or []
    ..      n/a
    //      ..
    *       *
    @       n/a
    []      []
    |       [,]   
    []      ?()
    n/a     ()
    ()      n/a


"""