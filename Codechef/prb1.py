X, Y = input().split()
X = int(X)
Y = float(Y)

if(X%5 == 0) and (X+ 0.50 <= Y):
    print("{:.2f}".format(Y - (X+0.50)))

else:
    print(Y)
    

