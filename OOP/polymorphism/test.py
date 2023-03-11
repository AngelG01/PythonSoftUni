from math import pi


class Shape:

    def calculate_area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * (self.radius ** 2)


class Rectangle(Shape):

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def calculate_area(self):
        return self.side_a * self.side_b


class Triangle(Shape):

    def __init__(self, base_length, height):
        self.base_length = base_length
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base_length * self.height


c = Circle(5)
r = Rectangle(10, 20)
t = Triangle(4, 3)

print(c.calculate_area())
print(r.calculate_area())
print(t.calculate_area())
