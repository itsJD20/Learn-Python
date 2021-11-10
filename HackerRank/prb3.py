l = list(map(int, input("ent: ").split()))

s = 0
a = l[0]
b = l[0]
for i in range(len(l)):
    if l[i] < a:
        a = l[i]
    if l[i] > b:
        b = l[i]
    s += l[i]






