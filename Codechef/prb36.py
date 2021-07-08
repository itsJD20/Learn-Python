def gcd(x,y):
    if y == 0:
        return x
    return gcd(y, x%y)

# 1 
# 3 5 10 15

T= int(input())
for i in range(T):
    
    l = list(map(int, input().split()))
    n = l[0] #3
    l = l[1:] #5,10,15

    if n == 1:
        print(1)
    
    elif n == 2:
        g = gcd(l[0], l[1])
        print(l[0]//g, l[1]//g)
    
    else:
        g = gcd(l[0], l[1])
        for i in l[2:]:
            g = gcd(i, g)
        for i in range(len(l)):
            l[i] = l[i] // g #1, 2, 3
        
        for i in l:
            print(i, end = " ")

        print("")


