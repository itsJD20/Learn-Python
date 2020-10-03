a = int(input("Enter item 1:"))
b = int(input("Enter item 2:"))

if (a%b==0):
    print("b divides a")
elif (b%a==0):
    print("a divides b")
else:
    print("No one divides no one")