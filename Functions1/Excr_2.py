a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

def numbers(a, b):
    if(a>b):
        print("Largest", a)
        print("Smallest", b)

    elif(a<b):
        print("Largest", b)
        print("Smallest", a)

    elif(a==b):
        print("Largest", a)
        print("Smallest", b)

numbers(a, b)
    

