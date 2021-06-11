def gcd(a, b): #2, 10

    M = 1 #1
    for i in range(1,min(a,b)+1):
        if((a%i == 0) and (b%i == 0)): #2%1, 10%1
            M = i
    return M

N = int(input()) #10
count = 0
for i in range(1, N):
    if gcd(i,N) == 1:
        count +=1

print(count)



   
        



    



    
       





