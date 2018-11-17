# -*- coding: utf-8 -*-
import chardet
s = "hello"
print(s)
print(chardet.detect(s))

#  解码返回的不是字符串，是object()
#  s.encode("utf-8")是字符串，s.decode("utf-8")是Unicode类型
s1 = "hello"
print(s)
print(type(s1.decode('utf-8')))
print(chardet.detect(s1))


s2 = "中国o"

print(s2)
print(chardet.detect(s2))  # utf-8编码

#------------总结------------------
             #编码
"a"         #ascii
"中国"       # utf-8
u"s中国"      #unicode