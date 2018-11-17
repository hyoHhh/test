# -*- coding: utf-8 -*-
import selenium.webdriver

# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# dcap = dict(DesiredCapabilities.CHROME) #处理chrome浏览器抢
# dcap["phantomjs.page.setting.userAgent"]=()
# driver= selenium.webdriver.Chrome()
#

#---------------Chrome--------------


# options=selenium.webdriver.ChromeOptions()
# options.add_argument("lang=zh_CN.UTF-8")
# options.add_argument('user-agent="Mozilla"')


#---------------不加载图片--------------
options=selenium.webdriver.ChromeOptions()
prefs ={"profile.default_content_setting_values":{"images":2}}
options.add_experimental_option("prefs",prefs) #不加载图片
driver=selenium.webdriver.Chrome(chrome_options=options)
# driver.get("http://www.httpbin.org/user-agent")
driver.get("http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&word=%E7%85%A7%E7%89%87")
import time
time.sleep(10)
driver.quit()
