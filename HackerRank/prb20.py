a = int(input())#123

count = 0
n = 0
newa = a
while a != 0:
    n = a%10
    newa = a//10
   
if a%n ==0:
    count += 1
    


print(count)
