# -*- coding: utf-8 -*-
import urllib2
url = 'http://www.baidu.com/'

# urlopen(url,data=none,timeout)超时的秒

def download2(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0Query String Parametersview sourceview URL encoded'
    }
    # response=urllib2.urlopen(url,timeout=3)
    request=urllib2.Request(url,headers=headers)
    request.add_header("Connection","keep-alive")
    # print(type(response))
    # print(response.info())  # 包含网站请求的详细信息
    # print(response.read())  # 包含网站的源代码  read(100)  读取前一百个
    data = urllib2.urlopen(request).read()
    print(data)
    # print(response.code)  # 打印响应码
try:
    print(download2(url))
except Exception as e:
    print(e)


"""
<type 'instance'>
Date: Tue, 30 Oct 2018 21:37:01 GMT
Content-Type: text/html
Transfer-Encoding: chunked
Connection: Close
Vary: Accept-Encoding
Set-Cookie: BAIDUID=A8FC9084C08048DFD0BA312D16C2A310:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie: BIDUPSID=A8FC9084C08048DFD0BA312D16C2A310; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie: PSTM=1540935421; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie: delPer=0; path=/; domain=.baidu.com
Set-Cookie: BDSVRTM=0; path=/
Set-Cookie: BD_HOME=0; path=/
Set-Cookie: H_PS_PSSID=1469_25809_21090_18560_27400; path=/; domain=.baidu.com
P3P: CP=" OTI DSP COR IVA OUR IND COM "
Cxy_all: baidu+ba84e15be3b229f02c58969b6b8985a9
Cache-Control: private
Expires: Tue, 30 Oct 2018 21:36:28 GMT
Server: BWS/1.1
X-UA-Compatible: IE=Edge,chrome=1
BDPAGETYPE: 1
BDQID: 0x98eec0830000d884
"""