"""
n = int(input("Enter the number: "))

for i in range(n+1):
    if (i==0):
        print(1)
    else:
        count =1

        for j in range(1,i+1):

            count=count*j
        print(count)
    
""" 
n = int(input("Enter the number: "))#4

for i in range(n+1):#2
    if (i==0):
        print(1)
    else:
        count =1

        for j in range(1,n+1):#2
            count=count*i#2
            print(count)
    """ 
    1
    1
    1
    1
    1
    2
    4
    





    

    


    """