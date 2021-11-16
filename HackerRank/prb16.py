n = int(input()) #6
p = int(input()) #2


m1 = p//2
if n%2 ==1:
    m2 = (n - p)//2
else:
    m2 =(n-p+1)//2
        

print(min(m1, m2))