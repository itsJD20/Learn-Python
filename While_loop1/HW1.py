# Input a number n and find all Primes from 1 to n
# n = 10
# 2 3 5 7

n = int(input("Enter the number: "))#5

i = 1


while i <= n:#2
    j =1
    count =0
    while j <= i:
        if(i%j==0):
            count = count+1
        j += 1

    if(count==2):
        print(i)
    
    i+=1
            

        


        

        

    

    

        
