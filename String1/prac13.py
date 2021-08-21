"""
st1 = "abaklbk"
st2 = "pbplktt"
Ans = "apt"
"""
st1 = input()
st2 = input()
s1 = set()
s2 = set()
for i in st1:
    s1.add(i) #s1 ={a,b,k,l}

for  j in st2: #s2 ={p,b,l,k,t}
    s2.add(j)

s = (s1 - s2) | (s2 -s1) 
print(s)
print("".join(list(s)))