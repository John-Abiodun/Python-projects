#This program is a leap year checker

print("\n")
print("LEAP YEAR CHECKER")
print("\n")
    
year = int (input("Please input the year:"))

if year % 4 == 0:
    print(year, "is a leap year")

else:
    print(year, "is not a leap year")
