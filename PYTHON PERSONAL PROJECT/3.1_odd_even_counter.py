#This program decides if a users input is an odd or even number

print()
print("This program checks if a number is an odd number or an even number")
print()
number = float (input("Enter a number:\n"))
print()

#modulus
mod = number % 2

#odd/even checker
if mod == 0:
    print("{} is an EVEN number".format(number))
else:
    print("{} is an ODD number".format(number))
