a = input()

L = "" 
N = ""



for i in range(len(a)):
    
    if(a[i].isupper()):
        N = N + a[i]
    elif(a[i].islower()):
        L = L + a [i]

print(L, N)
    





