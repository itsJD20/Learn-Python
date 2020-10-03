a = int(input("Enter the number: "))

for i in range(a):
    for j in range(a):
        if(i==0):
            print("*",end=" ")
        elif(i==a-1):
            print("#",end=" ")
        else:
            print("0",end=" ")
    print("")