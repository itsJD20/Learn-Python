"""
st = "1010"
        |
    0*2^0 + 1*2^1 + 0*2^2 + 1*2^3    
Ans = 10

st = "111"
Ans = 7

"""
st = input() #10101

pt = len(st) - 1 
s = 0 #
for i in range(len(st)): #
    
    k = int(st[pt]) *(2**i)
    s += k


    pt -= 1

print(s)
        

