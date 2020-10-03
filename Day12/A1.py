n = int(input("Enter the number: "))#7

for i in range(n):#0
    
    for j in range(n-(i+1)):#6#0
        print("-", end="")
    
    for j in range(2*i+1):
        if(i==n-1 or j == 0 or j == 2*i):#6
            print(".", end = "")
        else:
            print(" ", end = "")

    for j in range(n-(i+1)):#6#0
        print("-", end="")
    print(" ")
