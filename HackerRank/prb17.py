t = int(input())#3

for m in range(t):#0
    ih = int(input())#2
    if ih == 0:
        print(1)
        
    else:

        for i in range(ih):#3

            l =[]
            for j in range(ih+1):
                l.append(j)
            h = 0
            for k in range(len(l)):#0
                if (l[k] ==0) or (l[k]%2 == 0):
                    h += 1
                elif l[k] %2 !=0:
                    h =h*2
        
        print(h) 

        




    




