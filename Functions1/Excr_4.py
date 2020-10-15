n = int(input("Enter the number: "))

def search_prime(number):

    count = 0
    for i in range(1,number+1):
        if(number%i==0):
            count = count+1
    return count == 2
    
    
val = search_prime(n)
if val:
    print("Prime")
else:
    print("Not Prime")





