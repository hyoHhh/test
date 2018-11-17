# -*- coding: utf-8 -*-



from aip import AipFace

""" 你的 APPID AK SK """
APP_ID = '14844983'
API_KEY = 'XV5SI5ejk8UGWP8igRkvE3Wa'
SECRET_KEY = '2L4VoMk3sUfj8Fs0p2mliT1gsGe1htAI'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('C:\Users\Administrator\Desktop\WebCrawler\day17\\6.jpg')


""" 如果有可选参数 """
options = {}
options["max_face_num"] = 2
options["face_fields"] = "age,beauty"

""" 带参数调用人脸检测 """
final=client.detect(image, options)
print(final)

