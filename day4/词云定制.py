# -*- coding: utf-8 -*-
import jieba # 分词
import numpy as np #科学计算
import matplotlib.pyplot as plt  #数据可视化
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS #词云，颜色生成器，截止词语

from PIL import Image  #处理图片

textfile = open("rsa.txt",'rb') #读取文本内容
textfile=textfile.read()
# wordlist = jieba.cut(textfile,cut_all=True) #切割
wordlist = jieba.cut_for_search(textfile) #切割

space_list = " ".join(wordlist) #链接词语

backgroud = np.array(Image.open("2.jpg"))  #背景图片

mywordcloud=WordCloud(background_color="pink",#北京颜色
                      mask=backgroud,#写字用的背景图，从背景图取颜色
                      max_words=40,#最大词语数量
                      stopwords=STOPWORDS, #停止的词语
                      font_path="simkai.ttf", #字体类型
                      max_font_size=100,  #字体大小
                      random_state=30, #随机角度
                      scale=1,
                      ).generate(space_list) #生成词云

image_color = ImageColorGenerator(backgroud) #生成词云的颜色
plt.imshow(mywordcloud)   #显示词云
plt.axis("off") #不保存图片，关闭保存
plt.show() #显示图片





