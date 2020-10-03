a = int(input("Enter the number: "))

for i in range(a):
    for j in range(a):
        if(i==0 or i==a-1 or j==0 or j==a-1 or i==j or j==a-1-i):
            print(1,end=" ")
        else:
            print(0,end=" ")
    print("")



"""
a = 6

1 1 1 1 1 1
1 1 0 0 1 1
1 0 1 1 0 1
1 0 1 1 0 1
1 1 0 0 1 1
1 1 1 1 1 1
"""