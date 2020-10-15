n = int(input("Enter the number: "))


S = 0


for i in range(1,n+1):#2
    S += ((-1)**(i-1))*(i**(i))
    
print(S)