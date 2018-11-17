# -*- coding: utf-8 -*-
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '14836038'
API_KEY = 'grTm0iuaEnyjNn0XZriXGkKU'
SECRET_KEY = 'vUVtHedaEKmG8ecjWarhxSjmxWTBeIu7'



client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)




def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
print(client.asr(get_file_content(r'C:\Users\Administrator\Desktop\WebCrawler\day16\baiduAi\yuyinAi\auido.mp3'), 'mp3', 16000, {
    'dev_pid': 1536,
}))
