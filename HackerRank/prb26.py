n = int(input())

a = list(map(int,input().split()))

a.sort()
a = a[::-1]
s =0
for i in range(len(a)):
    s += 2**i * a[i]
print(s)

