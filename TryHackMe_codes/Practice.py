numbers=[1,2,4,5,77,9,5,4,1,7]
n=[]

for i in range(len(numbers)):
    if numbers[i] not in n:
        n.append(numbers[i])
        n.sort()

print(n)
