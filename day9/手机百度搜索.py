# -*- coding: utf-8 -*-
from selenium import webdriver

import time

# 设置

# mobilesetting={"deviceName":"iPhone 8"}
# options=webdriver.ChromeOptions()#选项

# options.add_experimental_option("mobileEmulation",mobilesetting) #模拟手机

driver = webdriver.Chrome()
# driver.set_window_size(320,800)
driver.get('http://www.kugou.com/song/litny53.html?frombaidu?frombaidu#hash=238B786A3F93C42E3D212953E1CE96C3&album_id=0')
time.sleep(19)
# kw=driver.find_element_by_id('kw')
#
# kw.send_keys("体面")
# print("搜索成功")
# time.sleep(3)
# bn=driver.find_element_by_id('su')
# print("点击搜索")
# bn.click()
# time.sleep(3)
# pk=driver.find_element_by_xpath('//*[@id="1"]/div[1]/div/div[2]/div[2]/div[3]/a[@class="c-btn"]')
# print("进入播放页面")
#
# pk.click()
# time.sleep(7)
# print("准备点击播放")
# time.sleep(5)
# final=driver.find_element_by_xpath('//*[@id="kw"]')
# final.send_keys("体面 于文文")
# ok=driver.find_element_by_xpath('//*[@id="su"]')
# ok.click()
# time.sleep(30)
# print(driver.page_source)
# time.sleep(30)
# # time.sleep(5)
# ok2=driver.find_element_by_xpath('//*[@id="1"]/div[1]/div/div[1]/div/ul/li[5]')
# ok2.click()
# ok3=driver.find_element_by_xpath('//*[@id="1"]/div[1]/div/div[4]/div[1]/div/a[2]')
# time.sleep(30)
# ok3.click()
# time.sleep(30)
driver.find_element_by_css_selector('#toggle').click()
