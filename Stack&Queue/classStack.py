class Stack():

    def __init__(self,m):
        self.max = m
        self.l = 10
        self.top = -1

    def push(self, n):
        if self.top == m-1:
            print("Stack overflow")
            return
        self.top += 1
        self.l[self.top] = n 
        

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
            return
        self.top -= 1

    
    def peep(self):
        if self.top = -1:
            print("No element left")
            return
        return self.l[self.top]

    def display(self):
        for i in range(self.top,-1,-1):
            print(self.l[i])
        




        
            


   


        