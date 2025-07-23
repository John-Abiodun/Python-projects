import math
print("A program to calculate the area and circumference of a circle")

radius = float (input("What is the radius of the circle: "))
area = math.pi * (radius**2)
circum = 2 * math.pi * radius

print("The area of the circle is:", round(area, 2))
print("The circumference of the circle is:", round(circum, 2))
