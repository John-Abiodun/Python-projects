#THIS PROGRAM IS A BMI CALCULATOR

print("Welcome to the BMI calculator")
print("\n")

weight = float (input("Please enter your weight in kg\n"))
print("\n")

height = float (input("Please enter your height in meters\n"))
print("\n")

bmi = weight / (height * height)

if bmi < 18.5:
    print("\nYour BMI is", round(bmi, 3), "which indicates you might be underweight")

elif bmi >= 18.5 and bmi <= 24.9:
    print("\nYour BMI is", round(bmi, 3), "which indicates you are a healthy weight")

elif bmi >=25 and bmi <= 29.9:
    print("\nYour BMI is", round(bmi, 3),"which indicates that you may be overweight")

elif bmi >= 30:
    print("\nYour BMI is", round(bmi, 3), "which indicates that you may be obese")
