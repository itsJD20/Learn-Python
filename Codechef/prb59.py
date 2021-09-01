T = int(input())

for i in range(T):
    n = int(input())

    l = list(map(int, input().split())) # 1,2,3

   
    count = 0 #3
    for j in range(len(l)):  #2
        
        s = l[j] #3
        p = l[j] #3
        if s == p:
            count += 1
        

        for k in range(j+1, len(l)): #2
            s = s + l[k]
            p = p * l[k]

            if s == p:
                count += 1

    print(count)

    



