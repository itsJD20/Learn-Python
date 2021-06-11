phone = input("Phone:").lower().split()#1245
digits ={
    "one":   "1",
    "two":   "2",
    "three": "3",
    "four":  "4"
}

output = ""
for i in phone:#1
    #i = i.lower()
    if i not in digits:
        dig="!"
    else:
        dig=digits[i]
    output += dig +" "#one two four !

print(output)