def f(a):
    if a == 0:
        return 1
    return a*f(a-1)


n = int(input())
print(f(n))
