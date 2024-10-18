# class Area

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
    def area(self):
        area = self.length * self.width
        print(f"The area of the rectangle is: {area} cm2")
        

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
rectangle = Rectangle(length, width)

rectangle.area()