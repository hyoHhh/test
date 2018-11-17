# -*- coding: utf-8 -*-
import time

from selenium import webdriver

driver=webdriver.Chrome()  #配置参数
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("kw").submit()
# driver.get_cookies()#抓取cookie
# driver.get_cookie() #抓取特定的cookie
for line in driver.get_cookies():
    print(line)
time.sleep(5)



