n = int(input("enter the number: "))#5


for j in range(1,n+1):
    count=0
    for i in range(1,j+1):#3
        if(j%i==0):
            count=count+1


    if(count==2):
        print(j)


               

       