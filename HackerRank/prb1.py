l = list(map(int, input().split()))

n = len(l)
countpos = 0
countzero = 0
countneg = 0

for i in range(len(l)):
    if l[i] < 0:
        countneg += 1
    elif l[i] == 0:
        countzero += 1
    else:
        countpos += 1
    
print("{:.6f}".format(countpos/n))
print("{:.6f}".format(countzero/n))
print("{:.6f}".format(countneg/n))
