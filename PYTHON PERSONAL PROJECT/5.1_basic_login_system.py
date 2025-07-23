#This program is a basic login system

print("This program is a basic login system")
print()

name = input("Create a username")
passcode = input("Create a password")
print()

print("Welcome...")
print()

for attempt in range(3):
        print(f"Login attempt {attempt + 1} of 3")
        username = input("Please enter your username:")
        
        if name == username:
                print("Username correct")
                print()
                password = input("Enter your password")
        
                if password == passcode:
                         print("Password correct. LOGIN SUCCESSFUL")
                         break
                else:
                          print()
                          print("Password incorrect")
        else:
                print()
                print("Username Incorrect")
        
        if attempt < 2:
                print()
                print(f"Attempts left: {2 - attempt}\n")
        else:
                ()
                print("Trial exceeded. LOGIN DENIED!")
