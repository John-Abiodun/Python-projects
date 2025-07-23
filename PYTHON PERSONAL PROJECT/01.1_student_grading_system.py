#This program calculates the average of three subjects for a student and grades them

print()
print("This is a program that calculates the average of three subjects for a student and grades them based on the results.")
print()

#Get user inputs
name = input("What is the student's name? ")
maths = float (input("What is the student's score for Mathematics?"))
english = float  (input("What is the student's score for English?"))
biology = float (input("What is the student's score for Biology?"))

#Calculate the average
average = (maths + english + biology)/3

#Print result to screen
print("The student's name is", name)
print()
print("The student's score for Mathematics is", maths)
print()
print("The student's score for English is", english)
print()
print("The student's score for Biology is", biology)
print()
print("The average of the student's score is", average)
print()

#if statements for grades
if average >= 70:
    print("Excellent! {}'s grade is an A".format(name))
    
elif average >= 69 and average < 70:
    print("Very good! {}'s grade is a B".format(name))
    
elif average >= 50 and average < 60:
    print("Good! {}'s grade is a C".format())
    
elif average >=45 and average < 50:
    print("Fair! {}'s grade is a D".format(name))

elif average >=40 and average < 44:
    print("Weak! {}'s grade is an E".format(name))
    
elif average < 40:
    print("Fail! {}'s grade is an F".format(name))







