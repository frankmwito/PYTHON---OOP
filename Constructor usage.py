import math

class Circle:
    # Constructor to initialize radius
    def __init__(self, radius):
        self.radius = radius

    # Method to calculate circumference
    def circumference(self):
        circumference = 2 * math.pi * self.radius
        print(f"The circumference is: {circumference:.2f}")

    # Method to calculate area
    def area(self):
        area = math.pi * pow(self.radius, 2)
        print(f"The area is: {area:.2f}")

# Input for radius
radius = int(input("Enter the radius of the circle: "))

# Create a Circle object
circle = Circle(radius)

# Call methods to display circumference and area
circle.circumference()
circle.area()
