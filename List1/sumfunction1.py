def sqr(x):
    return x**(1/2)


l = list(map(sqr, map(int, input().split())))

s = sqr(sum(l))

print (s)