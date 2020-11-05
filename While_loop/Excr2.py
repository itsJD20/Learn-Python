#Calculate factorial of all elements in a list

def cal_fact(n):

    fact = 1

    for i in range(n):
        fact = fact * i
    return fact 

l = list(map(int, input("Input numbers:").split()))
#print(l)
i = 0

while i < len(l):
    print(cal_fact(l[i]))
    
    
    
    i+=1

# 1 2 6 24 120 