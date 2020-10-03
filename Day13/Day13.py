n = int(input("Enter the number: "))#7


for i in range(n):#5
    
    for j in range(i+1):#6
        print(1,end =" ")

    for j in range(-2*i+(n-2)*2+1):
        print(" ",end=" ")

    for j in range(i+1):#3

        if(i==n-1 and j==n-1):
            print(" ",end=" ")
        else:
            print(1,end=" ")
        
        
    print(" ")
