a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = int(input("Enter the number 3: "))
d = int(input("Enter the number 4: "))

if a>b:
    s1=sum(list(range(b+1,a)))
else:
    s1 = sum(list(range(a+1,b)))
    

if c>d:
    s2 = sum(list(range(d+1,c)))
else:
    s2 = sum(list(range(c+1,d)))


if s1>s2:
    print (sum(list(range(s2+1,s1))))
else:
    print (sum(list(range(s1+1,s1))))
