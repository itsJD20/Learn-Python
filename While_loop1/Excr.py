#Input a number n and print all powers of 2 from 1 to n
#n = 15
#1 2 4 8

n = int(input("Enter the number: "))
i = 1
l = []


while i < n+1:
    l.append(i)
    

    i*=2

print(l)