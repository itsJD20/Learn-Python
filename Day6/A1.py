a = int(input("Enter the number: "))

for i in range(a):
    for j in range(i+1):
        if(i==j or i==(a-1) or j==0):
            print(1,end=" ")
        else:
            print(0,end=" ")

    print("")