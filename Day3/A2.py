a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = int(input("Enter the number 3: "))

if a>b:
    s = sum(list(range(b+1,a)))
else:
    s = sum(list(range(a+1,b)))


if c>s:
    print (sum(list(range(s+1,c))))
else:
    print (sum(list(range(c+1,s))))
