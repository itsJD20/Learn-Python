a = int(input("Enter the number: "))

for i in range(a):
    for j in range(i+1):
        if(j==0 or i==a-1):
            print(1,end=" ")
        else:
            print(0,end=" ")
    print("")




"""
a = 5

1
1 0
1 0 0
1 0 0 0
1 1 1 1 1
"""