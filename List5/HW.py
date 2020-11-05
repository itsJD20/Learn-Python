l1 = list(map(int, input("Enter L1 =").split()))
l2 = list(map(int, input("Enter L2 =").split()))
l3 = list(map(int, input("Enter L3 =").split()))

#l4 = []

#for i in range(len(l1)):
 #   l4.append(l1[i]+l2[i]+l3[i])

#print(l4)

l = [l1[i]+l2[i]+l3[i] for i in range(len(l1))]
print(l)