n = int(input())
s = list(map(int,input().split()))#1,2,1,2,1,3,2



for i in range(len(s)):#0
    count =0
    l =[]
    for j in range(len(s)):#0
        if s[i]== s[j]:
            count += 1
            if s[i] not in l:
                l.append(s[i])

        
            
    




