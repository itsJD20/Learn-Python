
d = int(input())
h = 0

for i in range(d+1):
    if i%2 == 0:
        h += 1
    else:
        h *= 2


print(h)

