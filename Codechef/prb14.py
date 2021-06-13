def fact(a):

    fact = 1
    for i in range(1,a+1):
        fact = fact * i

    return fact


T = int(input())

for i in range(T):

    N = int(input())


    print(fact(N))

