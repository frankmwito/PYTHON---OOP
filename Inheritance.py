# Inheritance

from abc import ABC, abstractmethod

class Vehicle(ABC):
    year = 2025  # Class variable
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @abstractmethod
    def move(self):
        pass
    
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
        
    def move(self):
        print(f"Car is moving")
        
    def __repr__(self):
        return f"Car details: Brand = {self.brand}, Model = {self.model}, Doors = {self.doors}, Year = {Car.year}"

# Input for car details
brand = input("Enter the brand of the vehicle: ")
model = input("Enter the model of the vehicle: ")
doors = int(input("Enter the number of doors of the vehicle: "))

# Create an instance of Car
car1 = Car(brand, model, doors)

# Call move method
car1.move()

# Print car details using __repr__
print(car1)

