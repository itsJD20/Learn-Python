class Blood():
    def __init__(self, bloodGroup, unitinHand):

        self.bloodGroup = bloodGroup.upper()
        self.unitinHand = unitinHand 


class BloodBank():
    def __init__(self, listofBlood):# A 10, B 5, O 2, AB 8, A- 2
        self.bloodList = listofBlood


    def isBloodAvailable(self, bloodGroup, noOfbloodRequire):# AB, 10
        count = 0
        for blood in self.bloodList:
            if blood.bloodGroup == bloodGroup:
                count += blood.unitinHand # 8

        if noOfbloodRequire <= count:
            return True
        else:
            return False

    def findMiniBloodStock(self):
        mini = self.bloodList[0].unitinHand #2
        for blood in self.bloodList: 
            if blood.unitinHand < mini:
                mini = blood.unitinHand #2
        L = []
        for blood in self.bloodList: # A 
            if blood.unitinHand == mini:
                L.append(blood.bloodGroup)
        return L
    
if __name__== "__main__":
    count = int(input())  # 5
    bl = []
    for i in range(count):# 5 # 1
        bloodType = input() # B
        bloodcount = int(input()) # 5
        blood = Blood(bloodType, bloodcount) # B 5
        bl.append(blood)

    bb = BloodBank(bl)
    bloodreq = input() # AB
    bloodreqCount = int(input()) # 10
    if bb.isBloodAvailable(bloodreq, bloodreqCount):
        print("Blood is Available ")
    else:
        print("Blood is not Available ")
    
    minlist = bb.findMiniBloodStock()
    for bloodname in minlist:
        print(bloodname)

'''
5
A
10
B
5
O
2
AB
8
A-
2
AB
10
'''






        

