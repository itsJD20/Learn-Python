n = int(input("Enter the number: "))

s=0
fact =1

for i in range(1,n+1):
    fact = fact*i
    s += (i**5)/fact

print(s)
