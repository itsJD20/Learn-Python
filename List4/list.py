l = list(map(int, input("Enter L =").split()))
l1 = []
length = len(l)
for i in range(1,length+1):
    
    l1.append(l[-i])

print(l1)


