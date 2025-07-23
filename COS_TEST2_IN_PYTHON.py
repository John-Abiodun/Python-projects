print("This program computes and displays the average scores and grades of students in three subjects")

#loop 
for i in range(5):
    print(f"~~~~~ Student {i+1} ~~~~~")

    #Get user input
    name =input("What is your name?")
    maths = float (input("Mathematics score:"))
    eng = float (input("English score:"))
    phy = float (input("Physics score:"))
    average = (maths + eng + phy) / 3

     #Print values to user            
    print("Student's name is:", name)
    print("The three subject scores are:", maths, ",", eng, "," ,phy)
    print("The average score is:", round(average, 2))

    #if else statements for grades
    if average < 45:
        print("Grade: F")
        
    elif average >= 45 and average < 50:
        print("Grade: D")

    elif average >= 50 and average <60:
        print("Grade: C")

    elif average >= 60 and average <70:
        print("Grade: B")

    elif average >= 70:
        print("Grade: A")

    print()


