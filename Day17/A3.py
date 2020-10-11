n = int(input("Enter the number: "))

S = 1

for i in range(1,n+1):
    S = i**2#1
    if(n==i):
        print(S, end =" ")
    else:
        
        print(S, end =",")

print(" ")
