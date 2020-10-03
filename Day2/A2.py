a,b,c = input("Enter the items: ").split( )
a,b,c = int(a),int(b),int(c)

if a<b and b>c:
    print("b is the largest number")
elif b<a and a>c:
    print("a is the largest number")  
else:
    print("c is the largest number") 