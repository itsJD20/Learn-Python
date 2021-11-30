n = int(input())#5

s = list(map(int, input().split()))#1 2 1 3 2
d,m = map(int, input().split())#3 2
i = 0       
count = 0  
while i < len(s)-(m-1):
    j = 0#1
    sm = 0#3
    while j < m:# 1<3
        sm += s[i+j] #0+1
        j+=1
    if sm == d:
        count += 1
    
    i += 1
    

print(count)


"""
1  2  3  4  5  6  1  2  3  

0 1 2 3                 4




"""




















9