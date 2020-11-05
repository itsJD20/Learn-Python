#write a program to accept a list from user and print list the square of the elements of the list

def sqr(x):
    return x**2


l = list(map(sqr, map(int, input("L = ").split())))


#l1 =[]

#for i in range(len(l)):
#    l1.append(l[i])

print(l)