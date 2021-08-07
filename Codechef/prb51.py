"""
n = 5
A = 2 5 3 7 8 
2 3 7 8                 cost - 2
2 7 8                   cost - 2 + 2
2 8                     cost - 2 + 2 + 2
2                       cost - 2 + 2 + 2 + 2

2
A = 2 3 7 8
4
2 7 8
6
2 8
8

(n-1) * min(A)
"""
T = int(input())
for j in range(T):
    n= int(input())
    A = list(map(int,input().split()))
    l =A[0]

    for i in range(len(A)):
        if A[i] < l:
            l = A[i]


        
    print((n-1)*l)












