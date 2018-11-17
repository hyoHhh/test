# -*- coding: utf-8 -*-


from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '14845303'
API_KEY = 'mrvitNoS7Gwlh5XdzaTx0MV0'
SECRET_KEY = 'Qpf9nB0wyXx6T4zBixOR54pd0KmBxDKk '

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


text = "百度是一家高科技公司"

""" 调用词法分析 """
print(client.lexer(text))

text = "百度是一家高科技公司"

# """ 调用词法分析（定制版） """
# client.lexerCustom(text);
#
#
# text = "张飞"
#
# """ 调用依存句法分析 """
# client.depParser(text);
#
# """ 如果有可选参数 """
# options = {}
# options["mode"] = 1
#
# """ 带参数调用依存句法分析 """
# client.depParser(text, options)