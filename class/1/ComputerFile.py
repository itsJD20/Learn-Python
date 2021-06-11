class Computer():

    def __init__(self, procs, mon): # Constructor
        self.processor = procs
        self.monitor = mon

    def printProcessor(self):
        print("Processor = ", self.processor)
    
    def printMonitor(self):
        print("Monitor = ", self.monitor)

    def printConfig(self):
        self.printProcessor()
        self.printMonitor()
if __name__ == '__main__':
    LG = Computer("i5", "Samsung") # Create LG object of class Computer

    LG.printProcessor()
    print(LG.monitor)
    LG.keyboard = "My Keyboard"
    #Dell = Computer("i3", "Nokia") # Create Dell object of class Computer

    #print("Config of LG")
    #LG.printConfig()

    #print("Config of Dell")
    #Dell.printConfig()


