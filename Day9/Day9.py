a = int(input("Enter Number: "))#4

for i in range(2*a-1):#6
    if (i<a):
        p = a-i-1
        q = i*2+1
    else:
        p = i - a + 1#3
        q = 2*(2*a-i)-3#

    for j in range(p):#2
        print(" ",end=" ")
    for j in range(q):#3
        print("*",end=" ")
    print("")



"""
      * 
    * * * 
  * * * * * 
* * * * * * * 
  * * * * * 
    * * *
      * 
      
"""