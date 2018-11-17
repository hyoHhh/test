# -*- coding: utf-8 -*-
from selenium import webdriver
url = 'https://www.kuaidaili.com/free/'
options=webdriver.ChromeOptions()
options.set_headless()
options.add_argument('--disable-gpu')

driver=webdriver.Chrome(options=options)
driver.get(url)
driver.implicitly_wait(10)
free_ip=driver.find_elements_by_xpath('//tbody/tr')
free_port=driver.find_elements_by_xpath('//tbody/tr')

for elem in free_ip:
    print(elem.find_elements_by_xpath('./td')[0].text)
    print(elem.find_elements_by_xpath('./td')[1].text)
driver.close()