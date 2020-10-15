n = int(input("Enter the number: "))#4

def cal_fact(num):

    fact = 1
    
    for i in range(1, num+1):
        fact = fact*i
       
    return fact



sum = 0
for i in range(1, n+1):

    sum += cal_fact(i)
print(sum)
