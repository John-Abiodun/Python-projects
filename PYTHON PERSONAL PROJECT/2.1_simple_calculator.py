#This is a simple calculator

print("Welcome to your calculator. This calculator rounds up to 5 decimal places.")
print()

number1 = float (input("What is the first number?"))
operator = input("Please choose an operator (+, -, /, *)")


#if statement for calculation

if operator == '+' :
    number2 = float (input("What is the second number?"))
    addition = number1 + number2
    print("Your first number is {}".format(number1))
    print("Your second number is {}".format(number2))
    print()
    print("{} / {}=" .format(number1, number2), round(addition, 5))

elif operator == '-':
    number2 = float (input("What is the second number?"))
    print()
    subtract = number1 - number2
    print("Your first number is {}".format(number1))
    print("Your second number is {}".format(number2))
    print()
    print("{} / {}=" .format(number1, number2), round(subtract, 5))

elif operator == '/':
    number2 = float (input("What is the second number?"))
    print()
    divide = number1 / number2
    print("Your first number is {}".format(number1))
    print("Your second number is {}".format(number2))
    print()
    print("{} / {}=" .format(number1, number2), round(divide, 5))

elif operator == '*':
    number2 = float (input("What is the second number?"))
    print()
    multiply = number1 * number2
    print("Your first number is {}".format(number1))
    print("Your second number is {}".format(number2))
    print()
    print("{} / {}=" .format(number1, number2), round(multiply, 5))

else:
    print("Invalid operator chosen. Please select '+' for addition, '-' for subtraction, '/' for division or '*' for multiplication")
                
