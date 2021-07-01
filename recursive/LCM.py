def gcd(x,y):

    if y == 0:

        return x
    x = gcd(y, x%y)
    return x

def LCM(x,y):
    return (x*y) // gcd(x,y)



A,B = map(int, input().split())

print(LCM(A,B))