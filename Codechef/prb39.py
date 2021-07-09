T = int(input())

for i in range(T):

    n,k = map(int, input().split())
    c = 0
    s = 0

    for i in range(1,k+1):
        c = n%i
        if c > s:
            s = c

    print(s)

        



        

