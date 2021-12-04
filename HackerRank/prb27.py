n = int(input())

a = list(map(int,input().split()))

a.sort()
m = 10**10
for i in range(len(a)):
    for j in range(i):
        if abs(a[i]-a[j]) < m:
            m = abs(a[i]- a[j])
print(m)