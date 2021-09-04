def isprime(a):

    count = 0

    for i in range(1,a+1):
        if a%i == 0:
            count += 1

    return count == 2

def list_sum(l):
    a = 0 #
    for i in range(len(l)): #1

        a += l[i]

    return a

def list_prime_sum(l):
    s = 0

    for i in range(len(l)):
        if isprime(l[i]):

            s += l[i]

    return s

    













