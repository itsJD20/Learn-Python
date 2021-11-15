s = int(input())
t = int(input())
a = int(input())
b = int(input())
m = int(input())
n = int(input())
app = list(map(int, input().split()))
org = list(map(int, input().split()))

l1 = []
l2 = []
for i in range(len(app)):
    l1.append(app[i]+a)

for i in range(len(org)):
    l2.append(org[i]+b)
c1 = 0
c2 = 0
for j in range(len(l1)):
    if l1[j] >= s and l1[j] <=t:
        c1 += 1
for j in range(len(l2)):
    if l2[j] >= s and l2[j] <= t:
        c2 += 1

print(c1,c2)


