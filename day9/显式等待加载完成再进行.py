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
# 如果元素出现，就继续，如果没有出现，所有操作最多十秒
elem = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.ID,'kw')))
# 最多等待十五秒,必须等到这个元素的出现
print(elem)
elem.send_keys("selenium")
time.sleep(19)
driver.close()