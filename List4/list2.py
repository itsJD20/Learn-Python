l = list(map(int, input("Input num: ").split()))
l1 = []
s = 0
for i in range(len(l)):
    s = s + l[i]
    l1.append(s)
print(l1)


