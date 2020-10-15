a = int(input("Enter the number: "))#1

def check_prime(num):#2

    count = 0
    for i in range(1,num+1):
        if(num%i==0):
            count = count+1

    return count==2


for i in range(1,a+1):#1
    if check_prime(i):
        print(i)


