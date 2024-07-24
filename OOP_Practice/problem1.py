import math

"""
  Write a  Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
Click me to see the sample solution
 """


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print(f"The area of the circle is: {math.pi * self.radius ** 2}")
    
    def perimeter(self):
        print(f"The perimeter of the circle is: {2 * math.pi * self.radius}")

circle = Circle(9)
circle.area()
circle.perimeter()
