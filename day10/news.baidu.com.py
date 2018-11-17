# -*- coding: utf-8 -*-
url = "http://news.baidu.com"
url2 = 'http://www.51shucheng.net/kehuan/santi/santi1/174.html'
import selenium.webdriver

driver=selenium.webdriver.Chrome()
driver.get(url2)


data=driver.find_elements_by_xpath("/*")
#  提取文本内容
for tag in data:
    print(tag.text)