def palin(x):

    if len(x) == 1:
        return True
    if len(x) == 2:
        if x[0] == x[-1]:
            return True
        else:
            return False
    return x[0] == x[-1] and palin(x[1:-1])







N = input()
print(palin(N))