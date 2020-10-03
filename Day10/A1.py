n = int(input("Enter the number: "))

for i in range(n):
    for j in range(n):
        if(i==0 and j==0 or i==0 and j==n-1 or i==n-1 and j==n-1 or i==n-1 and j==0):
            print(1,end =" ")
        else:
            print(0,end =" ")
    print(" ")