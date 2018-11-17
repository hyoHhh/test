# -*- coding: utf-8 -*-
# 抓取网页并编码解码
import chardet
import requests
import lxml
import lxml.etree
import re
url  = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='

def get_url(url):
    # page_txt=requests.get(url).text  #返回unicode
    page_txt=requests.get(url).content #返回str
    print(type(page_txt))
    print(chardet.detect(page_txt))
    return page_txt.decode("gb2312",errors='ignore')

rec=get_url(url)
txt=lxml.etree.HTML(rec)
print(txt.xpath("//div[@class='pagination']/text()"))
my_list=txt.xpath("//div[@class='pagination']/text()")
print(my_list[-1])
text=my_list[-1]
import re
pat=re.compile("\d+",re.IGNORECASE)
datalist=pat.findall(text)
print(eval(datalist[0]))
