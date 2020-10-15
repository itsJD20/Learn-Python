n = int(input("Enter the number: "))

def prime_check(num):

    count = 0
    for i in range(1,num+1):
        if(num%i==0):
            count = count+1

    return count == 2

sum = 0
for i in range(1, n+1):
    if(prime_check(i)):
        sum +=i
        print(prime_check(sum))


