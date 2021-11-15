l = list(map(int, input("ent: ").split()))

maxx = l[0]
count = 0
for i in range(len(l)):
    if l[i]> maxx:
        maxx = l[i]

for i in range(len(l)):
    if l[i] == maxx:
        count += 1




    


