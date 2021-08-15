"""
st1 = "abcdefx"
             |   
st2 = "adef"
          |
Ans = True

st1 = "abcdef"
st2 = "aefb"
Ans = False

find if the 2nd sting can be made by removing some characcters from the 1st string
"""
st1 = input()
st2 = input()
pointer1 = 0
pointer2 = 0 #4

while pointer1 < len(st1) and pointer2 < len(st2):
    if st1[pointer1] == st2[pointer2]:
        pointer1 += 1
        pointer2 += 1
    else:
        pointer1 += 1

if pointer2 == len(st2) :
    print(True)

else:
    print(False)


