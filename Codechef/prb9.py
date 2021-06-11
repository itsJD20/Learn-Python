def four(a): #41234
    

    count = 0#2
    s = 0 #3
    while a != 0:
        s = a % 10
        a//= 10
        if s == 4:
            count += 1
    return count
    


T = int(input()) #3

for i in range(T):
    t = int(input())
    
    
    print(four(t))
