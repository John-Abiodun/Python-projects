#This program is a multiplication table generator

print("Welcome to your muliplication table generator")
print()

number = int (input("Please enter the number to generate multiplication table for:"))

for multiply in range(1, 13):
    print( number, "*", multiply, "=", number * multiply)
    
