a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = int(input("Enter the number 3: "))

s = sum(list(range(a+1,b)))


#y = list(range(c+1,s,-1))

if c<s:
    print(list(range(c+1,s)))

else:
    print(list(range(s+1,c)))



