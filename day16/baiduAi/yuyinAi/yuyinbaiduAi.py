# -*- coding: utf-8 -*-
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '14836038'
API_KEY = 'grTm0iuaEnyjNn0XZriXGkKU'
SECRET_KEY = 'vUVtHedaEKmG8ecjWarhxSjmxWTBeIu7'



client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = client.synthesis('猪妹', 'zh', 1, {
    'vol': 5,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)
import mp3play
filename="auido.mp3"
player=mp3play.load(filename)
player.play()
import time
time.sleep(40)

#
# import pygame
#
# pygame.mixer.init()
# pygame.mixer.music.load(filename)
# pygame.mixer.music.play()
# import time
# time.sleep(10)


