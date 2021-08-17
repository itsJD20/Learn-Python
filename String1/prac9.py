"""
st = "1qazxsw@4"
Ans-----
number 2
character 6
special 1


st = "1qa"
Ans-----
number 2
character 6

"""

st = input()
numbers = 0
character = 0
special = 0
for i in st:
    if i.isnumeric():
        numbers += 1
    elif i.isalpha():
        character += 1
    else:
        special += 1

print(numbers)
print(character)
print(special)


