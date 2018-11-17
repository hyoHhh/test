# -*- coding: utf-8 -*-
import subprocess

p=subprocess.Popen([r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
                    r'C:\Users\Administrator\Desktop\识别图片\baidu.jpg',
                    r"baidu",
                    r'-l',
                    r'chi_sim',
                    ],
                   stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE,)
print("执行完毕")
p.wait()
file = open("baidu.txt",'r')
print(file.read())
