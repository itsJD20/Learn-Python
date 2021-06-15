def cal(b):
    return  b*(b+1)//2

 
T = int(input())

for i in range(T):
    D,N = map(int, input().split())
    

    for j in range(D):
        N = cal(N)

    print(N)


# 1+2+...+n = (n*(n+1))/2
# 1**2 + 2**2 + ...+ n**2 = (n*(n+1)*(2*n+1))/6
# 1**3 + 2**3 +...+ n**3 = ((n*(n+1))/2)**2

