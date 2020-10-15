x = int(input("Enter the number x: "))
n = int(input("Enter the number n: "))


s=1
fact =1

for i in range(1,n+1):
    fact = fact*i
    s += (x**i)/fact

print(s)