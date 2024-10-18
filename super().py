# Super() and method resolution Order(MRO)

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal Constructor: {self.name}")
        
class Mammal(Animal):
    def __init__(self, name, hair):
        super().__init__(name)  # Calls Animal's constructor
        self.hair = hair
        print(f"Mammal Constructor: Hair - {self.hair}")
        
    def display(self):
        print(f"Name: {self.name}, Hair: {self.hair}")
        
        
class Bird(Animal):
    def __init__(self, name, feathers):
        super().__init__(name)  # Calls Animal's constructor
        self.feathers = feathers
        print(f"Bird Constructor: Feathers - {self.feathers}")
        
    def display(self):
        print(f"Name: {self.name}, Feathers: {self.feathers}")

# Testing MRO and super()

# Create a Mammal object
mammal = Mammal("Elephant", "Thick Hair")
mammal.display()

# Create a Bird object
bird = Bird("Parrot", "Colorful Feathers")
bird.display()

# Checking the Method Resolution Order (MRO)
print(Mammal.mro())
print(Bird.mro())
