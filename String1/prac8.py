"""
st1 = "_-__-_-__--___-_"
                       |     
st2 = "-__-"
          |  
Ans =2

"""
st1 = input()
st2 = input()
ptr1 = 0 #14
count = 0
for i in range(len(st1)): #4
    
    ptr2 = 0 #
    while ptr1 < len(st1) and ptr2 < len(st2):
        if st1[ptr1] == st2[ptr2]:
            ptr1 += 1
            ptr2 += 1
        else:
            ptr1 += 1

    count += 1 #3

print(count)
        



















