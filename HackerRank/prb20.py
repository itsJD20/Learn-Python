a = int(input())#123

count = 0
n = 0
newa = a
while newa != 0:
    n = newa%10
    newa = newa//10
   
    if n != 0 and a%n ==0:
        count += 1
    


print(count)
