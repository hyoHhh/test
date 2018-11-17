# -*- coding: utf-8 -*-


import urllib2


try:
    # httpproxy=urllib2.ProxyHandler({"http":"lilejing:111111@192.168.0.1:80"})  #代理无需账号
    httpproxy=urllib2.ProxyHandler({"http":"10.36.132.56:808"})  #代理无需账号
    opener=urllib2.build_opener(httpproxy)  # 创建一个打开器
    request=urllib2.Request("http://www.baidu.com")    #  访问百度
    response=opener.open(request,timeout=10)   #  打开网页，内置代理服务器
    print(response.read())
    print("OK")
except Exception as e:
    print("No")
