n = int(input("Enter the number: "))

S = 1

for i in range(1,n+1):
    if(i==n):
        print(i,"*",(i+1), sep ="", end = " ")

    else:
        print(i, "*", (i+1), sep = "",end = ", ")

print(" ")