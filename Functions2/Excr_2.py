n = int(input("Enter the number: "))#1

def cal_fact(num):

    fact = 1
    for i in range(1, num+1):
        fact = fact*i
    return fact 

for i in range(1, n+1):
    print(cal_fact(i))



