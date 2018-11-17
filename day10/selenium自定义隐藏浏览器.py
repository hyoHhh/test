# -*- coding: utf-8 -*-
import pyvirtualdisplay
from selenium import webdriver

display = pyvirtualdisplay.Display()
#
display.start()
# 定制网页
options=webdriver.ChromeOptions()
options.add_argument('--disable-extensions') #禁止外部插件
options.add_argument('--profile-directory=Default')
options.add_argument('--incongnito')
options.add_argument('--disable-plugins-discovery')
options.add_argument('--start-maxminzed')
driver = webdriver.Chrome(options=options)
driver.delete_all_cookies()
driver.set_window_size(800,800)
driver.set_window_position(0,0)
print("Ok")
driver.get("http://www.baidu.com")

print(driver.page_source)

driver.close()


