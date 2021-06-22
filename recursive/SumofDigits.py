def digit(a):

    if a == 0:
        return 0
    x = digit(a//10) + a%10

    return x


N = int(input())
print(digit(N))