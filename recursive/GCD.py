def gcd(x,y):

    if y == 0:
        return x 
    return gcd(y, x%y)




A = int(input())
B = int(input())

print(gcd(A,B))
