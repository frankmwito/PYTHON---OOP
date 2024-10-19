# Operator Overloading

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    # Overloading the + operator   
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    # Display point coordinates
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    

# Create two points
point1 = Point(int(input("Enter x and y for Point 1:\n x: ")), int(input("y: ")))
point2 = Point(int(input("Enter x and y for Point 2:\n x: ")), int(input("y: ")))

# Add the points using the overloaded + operator
result_point = point1 + point2

# Display the result
print(f"The sum of the points is: {result_point}")