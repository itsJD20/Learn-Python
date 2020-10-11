n = int(input("Enter the number: "))

S = 1

for i in range(1,n+1):
    if(i==n):
        print(i,"/",(i+1),"\\",(i+2), sep ="")

    else:
        print(i,"/",(i+1),"\\",(i+2), sep = "")

print(" ")