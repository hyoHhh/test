# -*- coding: utf-8 -*-
import time

from selenium import webdriver

driver=webdriver.Chrome()  #配置参数
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
time.sleep(5)

js = "window.scrollTo(200,550);"

driver.execute_script(js)

