"""
write a class insect with attributes num_legs and num_wings 
and methods can fly which returns true if no. of wings is greater than 0 and even 
and method can walk if no. of legs greater than 2 and even
and method is dead if no. of wings 0 and no. of legs <= 2

"""
class Insect():
    def __init__(self,name,num_wings,num_legs):
        self.name = name
        self.num_wings = num_wings
        self.num_legs =  num_legs

    def canfly(self):
        return self.num_wings > 0 and self.num_wings % 2 == 0

    def canwalk(self):
        return (self.num_legs > 2 and self.num_legs % 2 == 0)

    def dead(self):
        return (self.num_wings == 0 and self.num_legs <= 2)


    




            


            
        