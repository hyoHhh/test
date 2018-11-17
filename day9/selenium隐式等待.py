# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
options=webdriver.ChromeOptions()  #实例化一个选项
options.set_headless()
# options.add_argument(‘--headless‘)
options.add_argument('--disable-gpu')  #给一个选项添加一个方法
driver=webdriver.Chrome(options=options)  #实例化这个方法
driver.get("https://www.baidu.com")   # 开始访问一个网站
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys("李乐靖")
driver.find_element_by_id("su").click()
if driver.find_element_by_class_name("nums").is_displayed():
    print(driver.find_element_by_class_name('nums').text)

time.sleep(30)
driver.close()
