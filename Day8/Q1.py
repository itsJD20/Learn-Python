"""
Input a number from the user and print all prime numbers   
from 2 to that  number
"""

a = (int(input("Enter the number: ")))

for i in range(2,a+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    if(count==2):
        print(i)