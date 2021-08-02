T = int(input())

for i in range(T):

    N = int(input())

    l = list(map(int, input().split()))

    z =1
    for j in range(len(l)):

        z = z^l[j]


    print(z)















    





