def sqr(x):
    return x**2

def cube(x):
    return x**30


l1 = list(map(cube, map(sqr, map(int, input("L1 =").split()))))
l2 = list(map(sqr, map(int, input("L2 =").split())))

l3= []

