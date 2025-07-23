#This program asks users for three subjects, calculates the average and grades them

print("This program asks users for three subjects, calculates the average and grades them")
print()

#Ask user for inputs
name = input("What is the student's name?")
subject1 = input("What is the first subject?")
subject2 = input("What is the second subject?")
subject3 = input("What is the third subject?")
score1 = float (input("What is the score for {}?".format(subject1)))
score2 = float (input("What is the score for {}?".format(subject2)))
score3 = float (input("What is the score for {}?".format(subject3)))

#Calculate average
average = (score1 +score2 + score3)/3

#Print output
print("Student's name is {}.".format(name))
print()
print("The first subject is {},".format(subject1), "and the score is{}.".format(score1))
print()
print("The second subject is {},".format(subject2), "and the score is {}.".format(score2))
print()
print("The third subject is {},".format(subject3), "and the score is {}.".format(score3))
print()
print("The average of the three subjects is {}".format(average))
print()

#Grading condtion
if average >= 70:
    print("Excellent! {}'s grade is an A!".format(name))

if average >= 60 and average < 70:
    print("Very good! {}'s grade is a B!".format(name))

if average >= 50 and average < 60:
    print("Good! {}'s grade is a C!".format(name))

if average >= 45 and average <50:
    print("Fair! {}'s grade is a D!".format(name))

if average >= 40 and average < 45:
    print("Weak! {}'s grade is an E!".format(name))

if average < 40:
    print("Fail! {}'s grade is an F!".format(name))

