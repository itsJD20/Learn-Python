#write a program to accept a list from user and print list the square of the elements of the list


def sqr(n):
    return n**2
l = list(map(int, input("Enter L = ").split()))
l1 = list(map(sqr, l))
print(l)
print(l1)