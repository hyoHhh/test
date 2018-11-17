# -*- coding: utf-8 -*-

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(3)
driver.implicitly_wait(10)#控制操作的时间在十秒之内  少用
driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()
time.sleep(3)
firstwin = driver.current_window_handle  #获取当前窗口
all_windows=driver.window_handles  #获取所有的窗口

# 选择注册的窗口
for win in all_windows:
    if win !=firstwin:
        driver.switch_to_window(win)
        print("切换成功")
        driver.find_element_by_id("TANGRAM__PSP_3__userName").send_keys("aaa25439999999")

        time.sleep(3)


driver.close()  #关闭当前
time.sleep(5)

driver.quit()   #关闭全部