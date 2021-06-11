course = list(input("Enter the string: "))


for i in range(len(course)):
    if course[i].isupper() == True:
    
        course[i] = course[i].lower()

    elif course[i].islower() == True:

        course[i]= course[i].upper()


print(''.join(course))

        



     


        

