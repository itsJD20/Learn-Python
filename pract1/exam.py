def swags(a):#4
    def add(p, q):
        return p+q
    def mul(b,d):

        return b*d
    if a%2 ==0:
        return add
    else:
        return mul


print(swags(4)(9,10))