n = int(input())
s = list(map(int, input().split()))

m1 = s[0]
m2 = s[0]
c1 = 0
c2 = 0
for i in range(len(s)):
    if s[i] < m1:
        m1 = s[i]
        c1 += 1
    if s[i] > m2:
        m2  = s[i]
        c2 += 1

print(c1, c2)


    