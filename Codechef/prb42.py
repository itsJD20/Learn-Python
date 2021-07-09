T = int(input())

for i in range(T):
    n,m,k = map(int, input().split())
    d1 = 0
    d2 = 0
   
    if n != m and n > m:
        d1 = n - m

        if d1 == k or k > d1:


            for j in range(1,d1+1):
                    

                m += 1

            print(n-m)

        else:
            for l in range(k):
                m += 1

            print(n-m)
    
    elif n != m and m > n:
        d2 = m-n
        
        if d2 == k or k > d2:

            for j in range(1,d2+1):

                n+=1

            print(m-n)
        else:
            for l in range(k):
                n += 1
            print(m-n)

    else:
        print(0)



    




   