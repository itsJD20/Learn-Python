n = int(input("Enter the number: "))#7

for i in range(n):#0
    
    for j in range(-i+n-1):#6#0
        print(" ", end="")
    print("/",end = "")

    for j in range(i):
        if(i==n-1):#6
            print("_", end = "_")
        else:
            print(" ", end = " ")

    print("\ ")
