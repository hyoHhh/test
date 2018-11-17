# -*- coding: utf-8 -*-

import urllib2

httpproxy=urllib2.ProxyHandler({"http":"lilejing:111111@192.168.0.1:80"})
opener=urllib2.build_opener(httpproxy)
request=urllib2.Request("baidu")
repesponse=opener.open(request)
print(repesponse)
