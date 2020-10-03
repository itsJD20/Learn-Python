n = int(input("Enter the number: "))#7


for i in range(n):#5
    
    for j in range(-1*i+n):#6
        print(1,end =" ")

    for j in range(i*2-1):
        print(" ",end=" ")
        
    for j in range(-1*i+n):
        if(i==0 and j==n-1):
            print(" ",end=" ")
        else:
            print(1,end=" ")
        
    print(" ")