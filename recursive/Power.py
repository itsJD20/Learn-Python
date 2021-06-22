def p(a,b):

    if a == 0:
        return 0
    if a == 1:
        return 1
    if b == 0:
        return 1

    return p(a, b-1)*a


A,B = map(int, input().split())
print(p(A, B))