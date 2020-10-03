n = int(input("Enter the number: "))

for i in range(1,n+1):
    for j in range(-1*i+n):
        print(" ", end= " ")


  
    for j in range(i):
        print(j+1,end=" ")

    for j in range(i):
        if(j==0):
            print("",end="")
        else:
            print(i+j,end=" ")


    print(" ")