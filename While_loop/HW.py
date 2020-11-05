# n = 4
# 1 
# 0 1
# 1 0 1
# 0 1 0 1   
n = int(input("Enter the number: "))#3
i = 0

while i < n:#1
    j = 0
    while j < i+1:
        if((i-j)%2 == 0):
            print(1, end = " ")
        else:
            print(0, end = " ")
        j += 1 

    print(" ")
    i += 1
    
 