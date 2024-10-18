# Abstract class

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side * self.side
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5*self.base*self.height
    
    
side = float(input("Enter the side measurements: "))
square = Square(side)

print(f"The area of the square is {square.area()}")

base = float(input("Enter the base measurements: "))
height = float(input("Enter the height measurements: "))
triangle = Triangle(base,height)

print(f"The area of the triangle is {triangle.area()}")