# -*- coding: utf-8 -*-

import  urllib2
# 302就是重定向
class RedirectHander(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        res = urllib2.HTTPRedirectHandler.http_error_301(self,req,fp,code,msg,headers)#重定向以后的地址
        res.status = code
        res.newurl=res.geturl() #geturl当前的url
        print res.newurl,res.status
        return res
opener=urllib2.build_opener(RedirectHander)

#返回了重定向的地址
opener.open("http://www.baidu.cn/")


# reponse = urllib2.urlopen("http://www.baidu.com/")
# 判断是否重定向
# print reponse.geturl()=="http://www.baidu.com/"