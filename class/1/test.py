from PersonFile import Person
from PetFile import Pet

class House():
    def __init__(self,people, pets, color):
        self.people = people
        self.pets = pets
        self.color = color
    
    def paint(self, color):
        self.color = color

    def party(self):
        for eachPerson in self.people:
            eachPerson.eat()

        for eachPet in self.pets:
            eachPet.eat()

    def fight(self):
        for eachPerson1 in self.people:
            for eachPerson2 in self.people:
                if eachPerson1 != eachPerson2:
                    eachPerson1.fight(eachPerson2)


        for eachPet1 in self.pets:
            for eachPet2 in self.pets:
                if eachPet1 != eachPet2:
                    eachPet1.fight(eachPet2)

    def details(self):
        print("---------------------------")
        print("Color =", self.color)
        print("All people: ")
        for eachPerson in self.people:
            eachPerson.details()
        print("All pets: ")
        for eachPet in self.pets:
            eachPet.details()


if __name__ == '__main__':
    P1 = Person("Joyo", "female")
    P2 = Person("Deb", " male")
    P3 = P1.haveSex(P2)

    persons = [P1, P2, P3]
   
    Pet1 = Pet("Devid", "White", "dog" )
    Pet2 = Pet("Tommy", "Brownis", "rabbit" )

    pets = [Pet1, Pet2]

    H1 = House(persons, pets, "Black")
    H1.paint("White")
    H1.party()
    H1.fight()
    H1.details()
    H1.persons[1].details()