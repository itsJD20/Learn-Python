'''
abcbca
l = 6
a = l//2
: a     -a : 
abc     bca
{a:1,   {a:1,
 b:1,    b:1,
 c:1     c:1
}        }
'''  

T = int(input())
for i in range(T):
    s = input()
    l = len(s)
    h = l//2
    s1 = s[:h]
    s2 = s[-h:]

    d1 ={}
    d2 ={}
    for i in s1:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1

    for i in s2:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1


    if d1 == d2:
        print("YES") 
    else:
        print("NO")

    

