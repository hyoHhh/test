# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)#控制操作的时间在十秒之内  少用
driver.find_element_by_id("kw").send_keys("python 培训")
texts = driver.find_elements_by_xpath("//div/h3/a")
for text in texts:
    print(text.text)