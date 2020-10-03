a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

for i in range(a):
    for j in range(b):

        if(i%2==0):
            print(1,end=" ")
        else:
            print(0,end=" ")

    print("")
    
    """
    
    1 1 1 1 1  
    0 0 0 0 0 
    1 1 1 1 1
    0 0 0 0 0
    1 1 1 1 1


    """
   
