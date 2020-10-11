n = int(input("Enter the number: "))

for i in range (n):
    for j in range(-1*i+n):
        print(" ", end =" ")
    for j in range(2*i+1):
        print(1, end = " ")
    for j in range(-2*i+2*n-3):
        print(" ", end = " ")
    for j in range(2*i+1):
        if (j==2*i and i==n-1):
            print(" ", end=" ")
        else:
            print(1, end=" ")   


    
    print(" ")
    