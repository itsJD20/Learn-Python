n = int(input("Enter the number: "))
s = 0
for i in range(1,n+1):#4
    fac = 1
    for j in range(1,i+1):#4
        fac = fac * j#6
    s = s + fac#10

print(s)