P,r,t = input("Enter items :").split( )
P,r,t = int(P),float(r),int(t)

I = P*(1+(r/100)*t)-P

if I>=1000:
    print("Loan not granted")
else:
    print("Loan granted")

    