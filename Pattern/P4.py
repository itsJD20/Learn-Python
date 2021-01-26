"""
n = 4
1
2 3
4 5 6
7 8 9 10
"""
a = int(input("Enter the number: "))
c = 1
i = 0
while i < a:
    j = 0
    while j < i+1:
        print(c, end = " ")
        c += 1
        j += 1

    print(" ")

    i += 1