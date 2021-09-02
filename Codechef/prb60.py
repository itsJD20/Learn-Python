T = int(input())

for i in range(T):
    a,b,n = map(int, input().split()) # 3 4 5

    #a = 3*2*2*2
    #b = 4*2*2

    
    if n%2 != 0:
        a *= 2
    

    if a >= b:
        print(a//b) 
    else:
        print(b//a)

    

