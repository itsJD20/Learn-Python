x = int(input("Enter the number: "))
n = int(input("Enter the number: "))

S = 1

for i in range(1,x+1):
    S += i**n

print(S)
