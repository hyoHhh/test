# -*- coding: utf-8 -*-
import jieba

mystr = "我今天早上遇到一个美女要电话，美女说你有病，我回答正是因为你我才害了相思病"

sg_list = jieba.cut(mystr,cut_all=True)  #普通切割 #sg_list是一个生成器
print("/".join(sg_list))

sg_list = jieba.cut_for_search(mystr) #按照搜索来切割

print("/".join(sg_list))
