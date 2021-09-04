from pkg2 import Insect

class Spider(Insect):

    def __init__(self, name, num_wings, num_legs):
        super().__init__(name, num_wings, num_legs) #super class

    def canWeb(self):
        return True

spider = Spider("debayan", 0, 8)

print(spider.canfly())
print(spider.canwalk())
print(spider.dead())
print(spider.canWeb())
