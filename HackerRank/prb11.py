n,k = map(int,input().split())#6,3

arr = list(map(int, input().split())) #1,3,2,6,1,2

count =0 #2
for i in range(len(arr)):#1
    for j in range(len(arr)):#0
        if arr[i] < arr[j] and ((arr[i] + arr[j]) %k ==0):
            count+= 1

print(count)
