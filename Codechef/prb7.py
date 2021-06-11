def firstlastdigit(a):#123
    l = a % 10
    
    while a > 9:
        a//= 10
    l += a
    return l


T = int(input())

for i in range(T):

    N = int(input())

    print(firstlastdigit(N))

