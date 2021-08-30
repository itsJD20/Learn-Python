T = int(input())

for i in range(T):
    S = input()# bghggd

    d = {}

    for i in S:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    for j in d:
        if d[j] > l:
            l = d[j]

    print(l)

