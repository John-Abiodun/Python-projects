#This program calculates simple interest

print("This is a program to calculate simple interest")
print()

principal = float (input("Please enter the principle amount:"))
print()
rate = float (input("Please enter the rate:"))
print()
time = float (input("Please enter the time:"))
print()

interest = (principal * rate * time)/100

print("The simple interest is on {}".format(principal), "at {}%".format(rate), "for {} years".format(time), "is", round(interest, 3))

            
