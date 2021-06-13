T = int(input())

for i in range(T):

    N = int(input())

    if(N%2 == 0):
        print((N//2) +1)

    else:
        print((N-1)//2 + 1)