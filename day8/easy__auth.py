# -*- coding: utf-8 -*-
import pytesseract

from PIL import Image

image = Image.open('takin.png')
image.show()

# vcode = pytesseract.image_to_string(image)
#
# print (vcode)