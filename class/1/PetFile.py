'''
Create a class Pet.

A Pet has 4 attributes:
    name
    color
    typeOfAnimal
    health

Pet can do 4 things:
    eat:
        When a Pet eats his health increases by 8
    fight:
        When a pet fights his health reduces by 4
    play:
        Accept a toy from the user and check if the animal 
        can play with the toy. If the animal can play with the 
        toy it's health increases by 2

        Compatibility of toys and animals:
            dog can play with all toys
            parrots can play with bells
            rabbit can play with balls and bells
            other pets cannot play
    details:
        Prints all attributes of the Pet

When we create a new Pet we accept name, color and typeOfAnimal form 
the user and give it a health of 50.
''' 


class Pet():
    def __init__(self, name, color, typeOfAnimal):
        self.name = name
        self.color = color
        self.typeOfAnimal = typeOfAnimal
        self.health = 50

    def eat(self):
        self.health += 8

    def fight(self, otherAnimal):
        self.health -= 4
        otherAnimal.health -= 4

    def play(self, toy):
        if  self.typeOfAnimal == "dog":
            self.health +=2
        elif self.typeOfAnimal == "parrot" and toy == "bell":
            self.health += 2
        elif self.typeOfAnimal == "rabbit" and (toy == "ball" or toy == "bells"):
            self.health += 2

    def friend(self, otherAnimal):
        self.health += 12
        otherAnimal.health += 12



    def details(self):
        print("-----------------------")
        print("Name = ", self.name)
        print("Color =", self.color)
        print("Type of Animal =", self.typeOfAnimal)
        print("Health =", self.health)


if __name__ == '__main__':
    P1 = Pet("Devid", "White", "dog" )
    P2 = Pet("Tommy", "Brownis", "rabbit" )

    P1.eat()
    P2.eat()

    P2.play("ball")
    P1.fight(P2)
    P1.fight(P2)

    P2.friend(P1)

    P1.details()
    P2.details()



    



     