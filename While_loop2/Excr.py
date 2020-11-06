# input a list l and find factorial of each element of the list




def cal_fact(n):
    fact = 1
    i = 1

    while i <= n:
        fact *= i

        i+=1

    return fact 

l = list(map(cal_fact, map(int, input("Enter numbers:").split())))

print(l)


    