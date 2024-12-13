import math

class Polygon:
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

rectangle = Rectangle(5, 3)
triangle = Triangle(4, 7)

print(f"Area of the rectangle: {rectangle.area()}")
print(f"Area of the triangle: {triangle.area()}")
