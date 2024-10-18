# Method overriding

from abc import ABC,abstractmethod

class Animal(ABC): # Inherit from ABC to use abstract methods
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        return f" {self.name} the dog woofs!!!"
    
class Cat(Animal):
    def sound(self):
        return f" {self.name} the cat meows!!"
    
dog = Dog(name = input("Enter the dogs name: "))
cat = Cat(name = input("Enter the cats name: "))

print(dog.sound())
print(cat.sound())