#write a function to find whether a number is prime or not using while loop


n = int(input("Enter the number: "))

def prime(x):

    i = 1
    count = 0

    while i < x+1:
        if(x%i==0):
            count = count+1

        i+=1

    return(count==2)

print(prime(n))

    
        
