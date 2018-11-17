# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()  #配置参数
driver.get("http://www.baidu.com")

above=driver.find_element_by_link_text("设置")

ActionChains(driver).move_to_element(above).perform()  #鼠标停留
time.sleep(3)

driver.find_element_by_link_text("搜索设置").click()
time.sleep(3)


#操作下拉，引用控件
sel = driver.find_element_by_id("nr")
Select(sel).select_by_index(2)
driver.find_element_by_class_name("prefpanelgo").click()
driver.switch_to.alert.accept()  #解决网页提示

time.sleep(3)
driver.close()
