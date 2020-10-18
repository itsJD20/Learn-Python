def sqr(num):
    return num+2
    


a, b, c, d = map(sqr, map(int, input().split()))
print(a, b, c, d)