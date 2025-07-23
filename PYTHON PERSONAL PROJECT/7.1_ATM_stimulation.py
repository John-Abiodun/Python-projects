#This program is an ATM stimulation

print("Welcome to Bethel Bank. You can have only have a minimum account balance of 1000\n")
print()

password = int (input("Please create a 4 digit pin"))
print("Pin creation successful")
print()

balance = float (1000)

for pin_attempt in range(3):
    print(f"Login attempt {pin_attempt +1} of 3")
    pin = int (input("Please enter your 4 digit pin"))
    
    if pin == password:
            print("Login successful")
            print()
            while True:
                request = input("What do you want to do? Select:\n 1 to check balance\n 2 to deposit \n 3 to withdraw\n 4 to exit\n")
                print()
                if request == '1':
                    print(balance)
                    print()
                    break

                elif request == '2':
                    deposit = float (input("How much do you want to deposit?\n"))
                    if deposit > 0:
                        balance = float (deposit + balance)
                        print("Deposit successful! New balance =", balance)
                        print()
                    else:
                        print("Amount too low. Please enter an amount above 0")
                        print()

                elif request == '3':
                    withdraw = float (input("How much do you want to withdraw?\n"))
                    if balance > withdraw:
                        balance = float (balance - withdraw)
                        print("Withdrawal successful! New balance is", balance)
                        print()
                    else:
                        print("Insufficient funds.")
                        print()

                elif request == '4':
                    break
    
    else:
        print("Incorrect password.")

    if pin_attempt < 2:
            print()
            print(f"You have {2 - pin_attempt} attempts left")
    else:
            print("Pin trial exceeded. LOGIN DENIED!")
