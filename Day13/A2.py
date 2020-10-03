n = int(input("Enter the number: "))#5


for i in range(n):#0
    
    for j in range(n):#4
        if ((i+j)%2==0):
            print("-", end=" ")
        else:
            print("1", end=" ")

    print("")