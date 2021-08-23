"""
st1 = "ababbbbba"
st2 = "cdcdddddc"
Ans = True

st1 = "kwkwqwe"
st2 = "abcdefg"
Ans = False

1. st1[i] not in d
2. st1[i] in d and st2[i] == d[st1[i]]
3. st1[i] in d and st2[i] != d[st1[i]]
"""

st1 = input()
st2 = input()

match = True

d = {}

for i in range(len(st1)):

    
    if st1[i] not in d:
        d[st1[i]] = st2[i]
    elif st1[i] in d and st2[i] == d[st1[i]]:
        continue
    else:
        match = False
        break

if match:
    print(True)
else:
    print(False)





