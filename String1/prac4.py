"""
L1 = ["ab", "a", "xx", "pq"]
L2 = ["mb","pb","n","ab","xx"]

Ans = ["ab", "xx"]

Find common elements in a list
"""
L1 = input().split()
L2 = input().split()

l3 =[]

for i in range(len(L1)):
    for j in range(len(L2)):
        if L1[i] == L2[j]:
            l3.append(L1[i])
print(l3)

            
