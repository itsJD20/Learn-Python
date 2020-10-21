def duplicate(x):
    return x*2

l = list(input().split())#['abc','0', '8', '20' ]
l2 = list(map(duplicate, l))#['abcabc', '00', '88' '2020']
print(l2)
