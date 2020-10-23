l1 = list(map(int, input().split()))#1,2,3
l2 = list(map(int, input().split()))#4,5,6

l3 =[]

for i in range(len(l1)):
    l3.append(l1[i]+l2[i])

print(l3)

