def prime(a):

    count = 0
    for i in range(1,a+1):
        if(a%i == 0):
            count += 1


    return count

T = int(input())
for i in range(T):

    N = int(input())



    if(prime(N) == 2):

        print("yes")

    else:
        print("no")

