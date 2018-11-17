# -*- coding: utf-8 -*-
# from selenium import webdriver
# options = webdriver.FirefoxOptions()
# options.set_headless()
# options.add_argument('-headless')
# options.add_argument('--disable-gpu')
# driver=webdriver.Firefox(firefox_options=options)
# driver.get('http://httpbin.org/user-agent')
# driver.get_screenshot_as_file('takin.png')
#  截图某个网站的是图片
# driver.close()


from selenium import webdriver
options=webdriver.ChromeOptions()
options.set_headless()
# options.add_argument(‘--headless‘)
options.add_argument('--disable-gpu')

driver=webdriver.Chrome(options=options)
driver.get('http://www.baidu.com')
driver.get_screenshot_as_file('1.png')
print(driver.page_source)
driver.close()

