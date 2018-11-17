# -*- coding: utf-8 -*-
from selenium import webdriver
import os
url = 'https://pypi.python.org/pypi/selenium'
url2 = 'https://github.com/SeleniumHQ/selenium/tree/master/py'
options = webdriver.ChromeOptions()
# 设置文件下载
prefs = {"profile.default_content_setting.popups":0,
         "download.defalut_directory":r'C:\Users\Administrator\Desktop\爬虫实战\day10'}
options.add_experimental_option('prefs',prefs)
driver=webdriver.Chrome()
driver.get(url2)
driver.find_element_by_link_text("http://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.0.jar").click()

