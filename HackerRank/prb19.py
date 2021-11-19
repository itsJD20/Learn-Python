n = int(input())

k = 5
s = 2
for i in range(1,n):
    d = (k//2)*3
    s += (d//2)
    k = d

print(s)