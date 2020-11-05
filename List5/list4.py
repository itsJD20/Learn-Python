l =list(map(int, input().split()))#1 2 3 4

s = 0

for i in range(len(l)):#3
    s = s + l[i]# 10
    l[i] = s # 1 3 6 10
print(l)