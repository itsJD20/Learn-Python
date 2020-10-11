n = int(input("Enter the number: "))

for i in range(1,n+1):
    for j in range(-1*i+n):
        print(" ", end= " ")


  
    for j in range(2*i-1):
        print(j+1,end=" ")

    print(" ")