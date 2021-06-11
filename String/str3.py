course = input("Enter the string: ")
sub = input("Enter the string: ")
count =0 
for i in range(len(course)):

    if course[i:i+len(sub)]== sub:
        count += 1

print(count)




