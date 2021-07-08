def gcd(x,y):
    if y == 0:

        return x

    return gcd(y, x%y)

T = int(input())

for i in range(T):

    A,B = map(int, input().split())
    g = gcd(A,B)
    print(g, (A*B)//g)