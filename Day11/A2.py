n =(int(input("Enter the number: ")))

for i in range(n):
    for j in range(-i+n):
        print(3-i%3, end=" ")

    print(" ")