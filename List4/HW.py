def sqr(x):
    return x**2

l1 = list(map(sqr, map(int, input("L1 =").split())))
l2 = list(map(sqr, map(int, input("L2 =").split())))

l3= []

for i in range(len(l1)):
    if (i%2==0):
        l3.append(l1[i]+l2[i])

        print(l1[i]+l2[i])






