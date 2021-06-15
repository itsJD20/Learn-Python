T = int(input())

for i in range(T):
    p = int(input())
    count = 0
    num = 100
    if p >= num:

       
        count += p//num
        p = p% num

    num = 50
    if p >= num:

       
        count += p//num
        p = p% num

    num = 10
    if p >= num:

        
        count += p//num
        p = p% num

    num = 5
    if p >= num:

        
        count += p//num
        p = p% num

    num = 2
    if p >= num:
        count += p//num
        p = p% num

    num = 1
    if p >= num:
        count += p//num
        p = p% num


    print(count)



    

    





