T = int(input())

for i in range(T):
    n = int(input())
    s = input()
    
    
    d ={
        "Y": 0,
        "I": 0 
    }

    for i in s:
        if i in d:
            d[i] += 1
            
        else:
            d[i] = 1
            
    if d["I"] > 0 :
        print("INDIAN") 
    elif d["Y"] > 0 :
        print("NOT INDIAN")
    else:
        print("NOT SURE")







