def rev(s):

    if s == "":
        return ""

    x = s[-1] + rev(s[ : -1])
    return x

N = input()

print(rev(N))
