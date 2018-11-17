# -*- coding: utf-8 -*-
import pytesseract
import pytesseract.pytesseract
import PIL

import PIL.Image

image = PIL.Image.open(r'C:\Users\Administrator\Desktop\WebCrawler\day16\baiduAi\test.PNG')

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

print(pytesseract.pytesseract.image_to_string(image,lang="chi_sim"))