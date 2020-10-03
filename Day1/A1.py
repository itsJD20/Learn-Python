V,R,T,n = input("Enter 4 items: ").split(" ")

V,R,T,n =int(V),int(R),int(T),int(n)

P = (V/R)**n - ((R/T)**(1/n))

print(P)