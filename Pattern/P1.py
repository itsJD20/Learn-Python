"""
n = 5
1
2 1
2 2 1
2 2 2 1
2 2 2 2 1 
"""
n = int(input("Enter the num: "))

i = 0

while i < n+1:
    j = 0
    while j < i+1:
        if(j == i):
            print(1, end = " ")
        else:
            print(2, end = " ")

        j += 1

    print(" ")


    i += 1



