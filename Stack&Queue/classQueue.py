class Queue():

    def __init__(self, m):
        self.max = m
        self.last = -1
        self.first = -1
        self.list = [0 for i in range(m)] 


    def add(self, x):
        if self.last == -1 and self.first == -1:
            self.last += 1
            self.first += 1
            self.list[self.last] = x

        elif self.last == self.max-1:
            print("Queue overflow")
        
        else:
            self.last += 1
            self.list[self.last] = x

    def remove(self):
        if self.last == -1 and self.first == -1:
            print("Queue underflow")

        elif self.last == self.first:
            self.last = -1 
            self.first = -1

        else:
            self.first += 1

    def display(self):
        for i in range(self.first, self.last+1):
            print(self.list[i])





if __name__ == "__main__":

    q = Queue(10)
    q.add(10)
    q.add(20)
    q.add(30)
    q.add(40)
    q.add(50)
    q.add(60)
    q.add(70)
    q.add(80)
    q.add(90)
    q.add(100)
    print(" ------------------------")
    q.display()
    q.remove()
    q.remove()
    q.remove()
    q.remove()
    print(" ------------------------")
    q.display()
    q.remove()
    q.add(5)
    print(" ------------------------")
    q.display()








        

    
        

        
            