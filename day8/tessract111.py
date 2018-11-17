# -*- coding: utf-8 -*-
import subprocess

p=subprocess.Popen([r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',r'C:\Users\Administrator\Desktop\爬虫实战\day8\takin.png','last'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p.wait()
file = open("last.txt",'r')
print(file.read())
