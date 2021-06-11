n = int(input())

for i in range(n):
    s= input("")
    if(
        (len(s) >= 2 and s[-2:] == "ch") or 
        (
            len(s) >= 1 and 
            (
                s[-1:] == "x" or
                s[-1:] == "s" or
                s[-1:] == "o" 
            )
        )
    ):
        print(s+"es")
    elif (len(s) >= 2 and s[-2:] == "fe"):
        print(s[:-2]+"ves")
    elif(len(s) >= 1 and s[-1:] == "f"):
        print(s[:-1] + "ves")
    elif(len(s) >= 1 and s[-1:] == "y"):
        print(s[:-1]+"ies")
    else:
        print(s+"s")


    
