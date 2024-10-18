# Instance variables vs  class variables

class Car:
    num_wheels = 4
    car_year = 2025
    num_of_cars = 0
    def __init__(self, name, make, horse_power):
        self.name = name
        self.make = make
        self.horse_power = horse_power
        Car.num_of_cars += 1
        
    def start(self):
        print(f"{self.name} is starting")
        
    def stop(self):
        print(f"{self.name} is stopping")
    
name1 = input("Enter the name of car: ")
make1 = input("Enter the make of the car: ")
horse_power1 = int(input("Enter the horse power of the tunned car: "))

car1 = Car(name1, make1, horse_power1)

name2 = input("Enter the name of car: ")
make2 = input("Enter the make of the car: ")
horse_power2 = int(input("Enter the horse power of the tunned car: "))

car2 = Car(name2, make2, horse_power2)

name3 = input("Enter the name of car: ")
make3 = input("Enter the make of the car: ")
horse_power3 = int(input("Enter the horse power of the tunned car: "))

car3 = Car(name3, make3, horse_power3)

car1.start()
car2.stop()

print(Car.num_of_cars)