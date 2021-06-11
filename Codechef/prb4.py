def digits(a): #12345
    s= 0#5

    while a != 0:#1
        s += (a%10)
        a //= 10

    return s


T = int(input())

for i in range(T):

    N = int(input())

    print(digits(N))

    