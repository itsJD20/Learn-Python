def SOL(l):

    if l == []:
        return 0

    x = SOL(l[:-1]) + l[-1]
    return x


N = list(map(int, input().split()))

print(SOL(N))