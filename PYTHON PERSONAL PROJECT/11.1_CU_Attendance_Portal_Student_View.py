#This is an attempt at duplicating Covenant University Attendance Portal without the persistence

import random
import time

#Account creation
first_name = input("Please enter your first name\n")
last_name = input("Please enter your last name\n")

#generate username
id_rand = str (random.randint(1, 9999)).zfill(4)
letter = first_name[0]
student_id = str(250) + id_rand
create_username = letter + last_name + '@' + student_id
 
#password creation
create_password = input("Please create a password:\n")

print("\n")
print("Account creation successful. Your login details are:\n Username:", create_username.lower(), "\n Student id:", student_id, "\n Password: Your chosen password")
print("\n")

#Login
while True:
    username = input("Please enter your username or student id:\n")
    if create_username.lower() == username.lower() or student_id == username:
        print("Username Correct.")
        while True:
            password = input("Please enter your password:\n")

            #password checker
            if create_password == password:
                print("Password correct")
                print("\n")
                print("Welcome to your Portal", first_name, last_name)
                print("\n")
                break
            else:
                print("Incorrect password. Please try again")
        break
    else:
        print("Incorrect username. Please try again")
            

#attendance dashboard
tmc = "Not marked"
ams = "Not marked"
gst = "Not marked"
ent = "Not marked"
while True:
    print("1. Mark attendance")
    print("2. View attendance")
    print("3. Logout")
    option = input("Choose an option\n")
    
    #mark attendance
    print("\n")
    if option == '1':
            while True:
                print("\n")
                print("1. TMC")
                print("2. AMS")
                print("3. GST")
                print("4. ENT")
                print("5. Back")
                course = input("Please select a course:\n")
                print("\n")

                #tmc
                if course == '1' or course.lower() == 'tmc':
                    tmc = input("Select:\n 0 for absent \n 1 for present\n")

                #ams
                elif course == '2' or course.lower() == 'ams':
                    ams = input("Select:\n 0 for absent \n 1 for present\n")
                    
               #gst
                elif course == '3' or course.lower() == 'gst':
                    gst = input("Select:\n 0 for absent \n 1 for present\n")

                #ent
                elif course == '4' or course.lower() == 'ent':
                    ent = input("Select:\n 0 for absent \n 1 for present\n")

                elif course == '5' or course.lower() == 'exit':
                    break

                else:
                    print("Invalid course. Try again")
                    continue

    #view attendance
    elif option == '2':
            print("Attendance sumary for", first_name)
            print("TMC:", "Present\n" if tmc == "1" else "Absent\n" if tmc == '0' else "Not marked\n" )
            print("AMS:", "Present\n" if ams == "1" else "Absent\n" if ams == "0" else "Not marked\n")
            print("GST:", "Present\n" if gst == '1' else "Absent\n" if gst == '0' else "Not marked\n")
            print("ENT:", "Present\n" if ent == '1' else "Absent\n" if ent == '0' else "Not marked\n")
            print("\n")
            

    else:
            if option == '3':
                print("\nLogging out...")
                time.sleep(2)
                print("\nGoodbye,", first_name)
                break

