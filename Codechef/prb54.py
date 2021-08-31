T = int(input())

for i in range(T):
    S = input()# bghggd

    d = {} # s =2 a =1 b = 1


    for i in S:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    l = 0
    for j in d:
        if d[j] > l:
            l = d[j]

    if l == len(S) -l:
        print("Yes")
    else:
        print("No")





