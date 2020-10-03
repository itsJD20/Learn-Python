m,r,t,x,a,b = input("Enter 6 items:").split( )

m,r,t,x,a,b = int(m),int(r),int(t),int(x),int(a),int(b)

y = m*(r*t + 1/x)**(a/b)

print(y)