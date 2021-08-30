T = int(input())

for i in range(T):
    d =  list(map(int, input())) #1 0 1
    count0 = 0 #1
    count1 = 0 #2

    for j in range(len(d)):#2

        
        if d[j] == 0:
            count0 += 1
        else:
            count1 += 1
        
        

    
    if count0 == 1 or count1 ==1:
        print("Yes")

    else:
        print("No")




        







   
    










    

    

