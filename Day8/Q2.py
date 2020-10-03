"""
Input a number from the user and print factorial
factorial(n) = 1*2*3*4*...*n
"""

n = int(input("Enter the number: "))
if n == 0:
    print(1)
else:
    count=1
    for i in range(1,n+1):
        count=count*i
        
        
    print(count)

