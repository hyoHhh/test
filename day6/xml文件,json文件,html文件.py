# -*- coding: utf-8 -*-
import lxml
import lxml.etree

text = """
<div>
    <ul>
        <li class="item-0"><a href="link1.html">天气</a></li>
        <li class="item-1"></li>
        <li class="item-2"></li>
        <li class="item-3"></li>
        <li class="item-3"></li>
        <li class="item-3"><span class="10086"></span>/li>
        <li class="item-3"><span class="10086"></span>/li>
    </ul>
</div>
"""

html = lxml.etree.HTML(text)
print(type(html))
print(lxml.etree.tostring(html))
ret = html.xpath("//ul/li/a/text()")  #双斜杠，所有元素，单斜杠，当前下面的元素
print(ret)

# 首先通过urllib2.Request(headers=headers)
# res.decode（"gbk"）.encode("utf-8)
# 再urllib2.urlopen() return res
# lxml.etree.HTML(res)
# ret.xpath("")


