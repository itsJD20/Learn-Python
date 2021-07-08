T = int(input())

for i in range(T):
    N = int(input())
    l = list(map(int, input().split()))
    s1 = l[0]
    p1 = 0

    for j in range(len(l)):

        if l[j] < s1:
            s1 = l[j]
            p1 = j
    s2 = 10 ** 10
    for k in range(len(l)):
        if k == p1:
            continue
        elif l[k] < s2:
            s2 = l[k]

    print(s1+s2)






