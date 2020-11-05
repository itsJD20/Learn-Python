def cal_fact(n):

    fact = 1

    for i in range(1,n+1):
        fact *= i
    return fact

l =list(map(cal_fact, map(int, input().split())))

print(l)