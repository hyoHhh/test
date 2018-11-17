# -*- coding: utf-8 -*-
class Lejing():
    def __init__(self,speed=None,age=None,height=None,good=None,habit=None):
        self.age=age
        self.height=height
        self.good=good
        self.habit=habit
        self.speed=speed
    # def __str__(self):
    #     return "什么鬼阿"+str(self.speed)
    def __repr__(self):
        return "你们好"+self.habit
    def run(self):
        if self.speed:
            print("lejing的速度是"+str(self.speed))
        else:
            print("lejing在爬没有速度")

li=Lejing(speed=18,habit="篮球")
li.run()
le=Lejing(habit="足球")
le.run()

