def fact(a):

    fact = 1
    for i in range(1, a+1):
        fact = fact * i

    return fact


t = int(input()) #2

for i in range(t):

    N = int(input())

    print(fact(N))
    