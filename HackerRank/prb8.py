y = int(input())
if y < 1918:
    if y%4 ==0:
        h = 12
    else:
        h = 13
elif y > 1918:
    
    if (y%4==0 and y%100 != 0) or (y%400 ==0):
        h = 256 - 244
    else:
        h = 256 - 243
else:
    h = 256 - (243 -13)



print(str(h)+"."+"09" +"."+str(y))
