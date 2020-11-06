n = int(input("Enter the number: "))


def cal_prime(x):

    i = 1
    count = 0

    while i < x+1:
        if(x%i==0):
            count = count+1

        i+=1

    return (count==2)

j = 0
while j <= n:
    if(cal_prime(j)):
        print(j)
    j += 1

