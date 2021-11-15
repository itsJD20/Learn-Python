n = int(input())
s = list(map(int,input().split()))#1,2,1,2,1,3,2

d ={}

for i in range(len(s)):#2
    if s[i] in d:
        d[s[i]] += 1
    else:
        d[s[i]] = 1

pair =0#2
for i in d:#3
    if d[i]>= 2:
        cal = d[i]//2
        pair += cal

print(pair)



    

            
    




