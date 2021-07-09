T = int(input())

for i in range(T):
    n,m,k = map(int, input().split())
    b,d = 0,0

    if n-m > 0:
        d = n-m
    else:
        d = m-n
    
    if k<d:
        b=k
    else:
        b=d
    
    
    
    
    print(d - b)
    