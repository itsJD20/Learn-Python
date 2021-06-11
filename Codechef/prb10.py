def reverse(a):
    s = 0
    l = 0
    while a!= 0:
        s = a%10
        l = (l*10) + s
        a//=10
    return l




T = int(input())

for i in range(T):
    t = int(input())
    
    print(reverse(t))