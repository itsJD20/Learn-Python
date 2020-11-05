def cal_sqr(x):
    return x**2


l=list(map(int, input("Input numbers:").split()))
l1 = []
s = 0

for i in range(len(l)):
    s += l[i]
    l1.append(s)

l2 = list(map(cal_sqr, l1))

print(l2)





