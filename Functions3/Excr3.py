a = int(input("Enter the num a: "))
b = int(input("Enter the num b: "))
c = int(input("Enter the num c: "))
d = int(input("Enter the num d: "))
e = int(input("Enter the num e: "))

def min(a1, b2):
    if(a1<b2):
        return a1

    else:
        return b2

def max(a1, b2):
    if(a1>b2):
        return a1

    else:
        return b2


m1 = max(a,b)
m1 = max(m1,c)
m1 = max(m1,d)
m1 = max(m1,e)


m = min(a,b)
m = min(m,c)
m = min(m,d)
m = min(m,e)


sum = m+m1


print(sum)








    