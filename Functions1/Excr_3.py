a = float(input("Enter the number: "))#10
b = float(input("Enter the number: "))#5

def numbers(a, b):#10,5
    if(a>b):
        return a/b
       

    else:
        return b/a
      

print("ans", numbers(a, b))