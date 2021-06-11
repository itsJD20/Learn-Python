#[5,6,7 ,8 ,9 ,10]
#top = 3
m = 10
L = []
top = -1
def push(ele):
    global top
    if top == m-1:
        print("stack overflow")
        return
    L.append(ele)
    top += 1

def pop():
    global top
    if top == -1:
        print("stack underflow")
        return
    ele = L[top]# 10, 9
    top -= 1
    return ele 

def peep():
    return L[top] #L[5]

def display():
    for i in range(top, -1, -1):
        print(L[i])

if __name__ == "__main__":
    push(5)
    push(6)
    push(7)
    push(8)
    push(9)
    push(10)
    print("---------display Start------------------")
    display()
    print("---------display End-------------------")
    print(peep())
    pop()
    pop()
    print("---------display Start-------------------")
    display()
    print("---------display End-------------------")




