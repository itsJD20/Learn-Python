a = int(input("Enter the number: "))

for i in range(a):
    for j in range(a):
        if(i==0 and j==0 or i==0 and j==a-1 or i==a-1 and j==0 or i==a-1 and j==a-1):
            print("@", end=" ")
        elif(i==0):
            print(1,end=" ")
        elif(i==a-1):
            print(4,end=" ")
        elif(j==0):
            print(2,end=" ")
        elif(j==a-1):
            print(3,end=" ")

        else:
            print(0, end=" ")
    print(" ")