#This program calculates the area and circumference of a circle

import math
print("This program calculates the area and circumference of a circle")

pi = math.pi

radius = float (input("What is the radius of the circle?"))

area = pi * (radius * radius)

circumference = 2 * pi * radius

print("The area of the circle is", round(area, 2))
print("The circumference of the circle is", round(circumference, 2))
