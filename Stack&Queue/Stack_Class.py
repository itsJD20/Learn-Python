"""
1. m l and top will be attributes 
2. push,pop, peep, display will be methods
3. the init function will accept a number and assign it to m, l will be empty list, top will be -1

"""

class Stack():

    def __init__(self, m):
        self.max = m
        self.l = [0 for i in range(m)]
        self.top = -1

    def push(self, n):
        
        if self.top == self.max-1:
            print("stack overflow")
            return
        self.top += 1
        self.l[self.top] = n

    def pop(self):
        if self.top == -1:
            print("stack underflow")
            return
        ele = self.l[self.top]
        self.top -= 1
        return ele

    def peep(self):
        return self.l[self.top]

    def display(self):
        print("___Display___")
        for i in range(self.top, -1, -1):
            print(self.l[i])
        print("___End___")
        


if __name__ == "__main__" :
    
    S = Stack(10)
    S.push(5)
    S.push(6)
    S.push(7)
    S.push(8)
    S.push(9)
    S.push(10)
    print(S.peep())
    S.pop()
    S.pop()
    S.push(5)
    print(S.peep())
    S.display()
'''
9  |1 |
8  |1 |<- top
7  |1 |
6  |1 |
5  |10|
4  |5 |
3  |8 |
2  |7 |
1  |6 |
0  |5 |
       

max = 10

''' 

        
