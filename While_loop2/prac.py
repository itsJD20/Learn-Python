#sum of digits 

n = int(input("Enter a number:  "))#123456789
copy = n#123456789

sm = 0

while copy > 0:
    d = copy%10#9
    sm = sm+d#0+9
    copy = copy//10#(12345678)


print(sm)




    

