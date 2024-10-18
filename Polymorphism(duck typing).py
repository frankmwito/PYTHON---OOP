# Polymorphism (duck typing)

from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} woofs!!!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows!!!"
    
    
class Bird(Animal):
    def speak(self):
        return f"{self.name} chirps!!!"
    

name1 = input("Enter the Dog's name: ")    
dog = Dog(name1)

name2 = input("Enter the Cat's name: ")   
cat = Cat(name2)

name3 = input("Enter the Bird's name: ")   
bird = Bird(name3)

print(dog.speak())
print(cat.speak())
print(bird.speak())