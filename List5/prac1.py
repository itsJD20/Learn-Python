l = list(map(int, input().split()))

s = 0

for i in range(len(l)):
    s += l[i]
    l[i] = s
print(s)


