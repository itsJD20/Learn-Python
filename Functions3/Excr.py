n = int(input("enter the number: "))

def check_prime(num):

    count =0
    for i in range(1, num+1):
        if(num%i==0):
            count = count+1

    return count ==2

def fact(num):

    fact = 1
    for i in range(1,num+1):

        fact = fact*i
    return fact
    

sum = 0
for i in range(1,n+1):
    if(check_prime(i)):
       sum += fact(i)

print(sum)
        

    