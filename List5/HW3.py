l = list(map(int, input("Input numbers:").split())) 

m = 1

for i in range(len(l)):
    m = l[i]*m

print(m)

