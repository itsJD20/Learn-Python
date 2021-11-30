b,n,m = map(int, input().split())

key = list(map(int, input().split()))#3,1
dri = list(map(int, input().split()))#5,2,8
mx = -1
for i in range(len(key)):#3
    for j in range(len(dri)):#5
        if key[i] + dri[j] <= b and key[i] + dri[j] > mx:
            mx = key[i] + dri[j]
print(mx)

        




            

            

            
            




    
            