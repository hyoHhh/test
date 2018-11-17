# -*- coding: utf-8 -*-
from selenium import webdriver

import time

url = "https://videojs.com/"  #视频组件

driver = webdriver.Chrome()
driver.get(url)
time.sleep(9)
vedio = driver.find_element_by_class_name('vjs-icon-placeholder')

vedio.click()
 #  完全加载
# print(driver.execute_script())
time.sleep(10)

driver.close()
