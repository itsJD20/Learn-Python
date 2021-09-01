T = int(input())

for i in range(T):
    n = int(input())

    A = list(map(int, input().split())) #1, 10, 15
    B = list(map(int, input().split())) #1, 10, 3

    count = 0
    
    init = 0


    for j in range(len(B)):
        final = A[j] #1
        if B[j] <= final - init:
            count += 1

        init = final

    print(count)

    



