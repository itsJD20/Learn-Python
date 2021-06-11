'''
Create a class Person.

A person has 4 attributes:
    sex
    health
    shirtColor
    numberOfKids

Person can do 3 things:
    eat:
        When a person eats his health increases by 15
    fight:
        When a person fights his health reduces by 10
    changeShirt:
        change shirt Accepts a color of a new shirt and replaces 
        current shirt color 
    details:
        Prints all attributes of the person

When we create a new person we accept sex as male or female, initialize his/her health to 100, shirt color to None, numberOfKids to 0
''' 

class Person():

    def __init__(self,name, sex):
        self.name = name
        self.sex = sex
        self.health = 100
        self.shirtColor = None
        self.numberOfKids = 0


    def eat(self):
        self.health += 15
        
    def fight(self, otherPerson):
        self.health -= 10
        otherPerson.health -= 10

    def haveSex(self, otherPerson):
        if self.sex != otherPerson.sex:
            self.numberOfKids += 1
            otherPerson.numberOfKids += 1
            return Person(self.name+" "+otherPerson.name, "female")
            
        else:
            print("No Baby")

    def changeShirt(self, newShirtcolor):
        self.shirtColor = newShirtcolor

    def details(self):
        print("--------------------------")
        print("Name             =", self.name)
        print("Gender           =", self.sex)
        print("Health Condition =",self.health)
        print("Shirt            =",self.shirtColor)
        print("Children         =",self.numberOfKids)
        print("--------------------------")

if __name__ == '__main__':
    P1 = Person("Joyo", "female")
    P2 = Person("Deb", "male")

    P1.eat()
    P1.fight(P2)

    print("After Fight P1")
    P1.details()
    print("After Fight P2")
    P2.details()

    P3 = P1.haveSex(P2)

    print("Baby")
    P3.details()
    P2.details()
    P1.details()
