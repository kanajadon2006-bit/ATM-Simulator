
# atm_simulator.py

# Simple ATM Simulator with PIN and Basic Banking Features

correct_pin = "1234"
attempts = 0
balance = 10000

# Login system with 3 attempts
while attempts < 3:
    pin = input("Enter your 4-digit PIN: ")
    if pin == correct_pin:
        print("PIN verified successfully!\n")

        # ATM Menu
        while True:
            print("\nWelcome to ATM")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                print("Your balance is:", balance)

            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                balance += amount
                print("Deposited successfully. New balance:", balance)

            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                if amount > balance:
                    print("Insufficient balance.")
                else:
                    balance -= amount
                    print("Withdrawn successfully. New balance:", balance)

            elif choice == "4":
                print("Thank you for using the ATM!")
                break

            else:
                print("Invalid choice. Try again.")

        break  # Exit login loop after successful session

    else:
        attempts += 1
        print(f"Incorrect PIN. Attempts left: {3 - attempts}")

if attempts == 3:
    print("Too many incorrect attempts. ATM blocked.")
