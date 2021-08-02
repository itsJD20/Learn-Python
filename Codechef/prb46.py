T = int(input())

for i in range(T):

    a,b = map(int, input().split())
    s = a+b #357
    print(s)
    d = {
        0: 6,
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6
    }
    f =0
    while s != 0:
        
        n = s%10
        if n in d:
            f = f + d[n]
        
        s //= 10


    print(f)


