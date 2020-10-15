x = float(input("Enter the number x: "))#1
n = int(input("Enter the number n: "))#5


s=0
fact =1

for i in range(1,n+1):#3
    s += (-1)**(n+1) * (x**(2*n+1))/fact#
    fact = fact*(2*i)*(2*i+1)

print(s)




#1