# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["font.sans-serif"]=["simhei"]
matplotlib.rcParams['font.family']='sans-serif'
# 可以把爬去到的数据对应到图表当中去，根据matplotlib这个数据可视化的第三方库
plt.bar([1],[123],label=u"广东",color='g')
plt.bar([2],[33],label=u"江苏",color='y')
plt.bar([3],[113],label=u"湖南")
plt.bar([4],[113],label=u"浙江")
plt.bar([5],[145],label=u"上海")
matplotlib.use("Agg")
plt.legend()  #绘制
# plt.show()   #显示
plt.savefig("1.jpg")
