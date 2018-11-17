# -*- coding: utf-8 -*-
from selenium import webdriver

import time

# 设置

mobilesetting={"deviceName":"iPhone 8"}
options=webdriver.ChromeOptions()#选项

options.add_experimental_option("mobileEmulation",mobilesetting) #模拟手机

driver = webdriver.Chrome(chrome_options=options)
driver.set_window_size(320,800)
#  driver.maximize_window()#全屏
driver.get("https://www.taobao.com")
time.sleep(5)
driver.get("https://www.jd.com")
time.sleep(5)
driver.back()  #后退
time.sleep(5)
driver.forward() # 前进
time.sleep(5)
driver.refresh()#刷新
driver.close()


