"""
n = 5
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
a = int(input("Enter the number: "))

i = 0 
while i < a+1:
    j = 0
    while j < i+1:
        print(j+1, end =" ")

        j += 1

    print(" ")

    i += 1
    

