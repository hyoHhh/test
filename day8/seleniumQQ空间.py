# -*- coding: utf-8 -*-
import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://qzone.qq.com")

time.sleep(5)

driver.switch_to_frame("login_frame")

elem = driver.find_element_by_id("switcher_plogin")
elem.click()
time.sleep(3)
user = driver.find_element_by_id("u")
password = driver.find_element_by_id("p")
login_button = driver.find_element_by_id("login_button")
user.send_keys("258956131")
password.send_keys("django2.01114")
login_button.click()
time.sleep(20)
driver.close()
