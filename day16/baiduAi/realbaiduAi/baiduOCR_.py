# -*- coding: utf-8 -*-
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '14836038'
API_KEY = 'grTm0iuaEnyjNn0XZriXGkKU'
SECRET_KEY = 'vUVtHedaEKmG8ecjWarhxSjmxWTBeIu7'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(r'C:\Users\Administrator\Desktop\WebCrawler\day16\baiduAi\realbaiduAi\test_pic\sina.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
# list_w=client.basicGeneral(image)['words_result']
list_w=client.basicAccurate(image)['words_result']
for i in list_w:
    for k in i.items():
        print(i['words'])

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"


""" 带参数调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image, options)

# url = "http//www.x.com/sample.jpg"
url = "http://www.lmth2013.com/validatecode.aspx"

""" 调用通用文字识别, 图片参数为远程url图片 """
web_acc=client.basicGeneralUrl(url);
print(web_acc)

# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url, options)


