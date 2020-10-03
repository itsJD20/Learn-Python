n = int(input("Enter the number: "))#7

for i in range(n):
    for j in range(2*i):
        print(" ",end = "")

    print("<>",end = "")    
    

    for j in range (-4*i+2 + 4*(n-2)):
        print(" ",end = "")
    

    if (i!=n-1):
        print("<>",end ="")
    print("")

    

    
    