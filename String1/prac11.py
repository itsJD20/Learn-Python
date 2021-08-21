"""
st1 = "abaklbk"
st2 = "pbplktt"
Ans = "apt"
"""
st1 = input()
st2 = input()

s = set()
for i in range(len(st1)):
    found = False
    ch = st1[i]
    for j in range(len(st2)):
        if ch == st2[j]:
            found = True
            break

    if not found:
        s.add(ch)

for i in range(len(st2)):
    found = False
    ch = st2[i]
    for j in range(len(st1)):
        if ch == st1[j]:
            found = True
            break

    if not found:
        s.add(ch)
        
print("".join(list(s)))
          

            

   


           

