# -*- coding: utf-8 -*-
import re
mystr = """<span class=\"search_yx_tj\">共<em>5830</em>个职业满足条件</span>"""

restr = '<em>(\\d+)</em>'
# 预编译
regex = re.compile(restr,re.IGNORECASE)
#
mylist = regex.findall(mystr)

print  mylist