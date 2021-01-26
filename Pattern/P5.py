"""
n = 4
1
3 2
6 5 4
10 9 8 7
"""
a = int(input("Enter the number: "))#4
c = 1
i = 0 
while i < a:#3
    j = 0
    while j < i+1:#3
        print(c+i-j, end = " ")#7

        j += 1#3

    print("")
    c += j#7
    i += 1#3
