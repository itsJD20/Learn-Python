def XOR(a, b):
    ans = [] 
    for i in range(len(a)):
        if(a[i] == b[i]):
            ans.append("0")
        else:
            ans.append("1")

    return ans

print("At Receiver Side")       
ld = int(input("length of the message:")) # length of the message 7
lg = int(input("length of generator:")) # length of generator 4
data = input("the message:") # the message 1010000
generator = input("the generator:") # the generator 1001

d = list(data) 
g = list(generator) 

d += ['0']*(len(g) - 1)
for i in range(ld): 
    print(i)
    print(d)
    if(d[i] == "0"): 
        pass
    else:
        x = XOR(g,d[i:lg+ i]) 
        for j in range(0, len(x)):
            d[i+j] = x[j]
       

rem = d[ld: ] 

ans = data + ''.join(rem)
print(rem) 

if ''.join(rem) == "000":
    print("This is error free")
else:
    print("This is an error")f