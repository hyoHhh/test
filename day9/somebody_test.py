#-*- coding: utf-8 -*-
from selenium import webdriver
import time
options=webdriver.ChromeOptions()
options.set_headless()
# options.add_argument(‘--headless‘)
options.add_argument('--disable-gpu')
driver=webdriver.Chrome(options=options)
driver.get('https://www.kxdao.net')
driver.implicitly_wait(1)
for i in driver.get_cookies():
    print(i)
savedCookies = driver.get_cookies()
driver2 = driver=webdriver.Chrome(options=options)
driver2.get('https://www.kxdao.net')
driver2.delete_all_cookies()
for cookie in savedCookies:
    # fix the problem-> "errorMessage":"Unable to set Cookie"
    for k in ('name', 'value', 'domain', 'path', 'expiry'):
        if k not in list(cookie.keys()):
            if k == 'expiry':
                t = time.time()
                cookie[k] = int(t) # 时间戳 秒
    # fix the problem-> "errorMessage":"Can only set Cookies for the current domain"
    driver2.add_cookie({k: cookie[k] for k in ('name', 'value', 'domain', 'path', 'expiry') if k in cookie})

driver2.get('https://www.kxdao.net')
driver2.implicitly_wait(1)
for i in driver2.get_cookies():
    print(i)