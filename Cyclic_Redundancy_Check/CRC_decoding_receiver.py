def XOR(a, b):#1,0,0,1 #1,0,1,0
    ans = [] #0,0,1,1
    for i in range(len(a)):#4 - 0
        if(a[i] == b[i]):
            ans.append("0")
        else:
            ans.append("1")

    return ans
        
ld = int(input()) # length of the message 7
lg = int(input()) # length of generator 4
data = input() # the message 1010000
generator = input() # the generator 1001

d = list(data) #[0,0,0,0,0,0,0,  0,1,1]
g = list(generator) #[1,0,0,1]

d += ['0']*(len(g) - 1)
for i in range(ld): #7 - 6
    #print(i)
    #print(d)
    if(d[i] == "0"): # 1==0
        pass
    else:
        x = XOR(g,d[i:lg+ i]) #d[6:4+6] #1,0,1,0
        for j in range(0, len(x)):#4 0,0,1,1
            d[i+j] = x[j]
        #print(x)

rem = d[ld: ] #7:
#print(rem)
#ans = data + ''.join(rem)
print(rem) #1010000011

if ''.join(rem) == "000":
    print("This is error free")
else:
    print("This is error")