T = int(input())
for i in range(T):
    
    q,p = map(int, input().split())

    if q > 1000:
        print("{:.6f}".format(q*p*0.9))
    else:
        print("{:.6f}".format(q*p))


