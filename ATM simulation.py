

import time

print("Please insert your card")
time.sleep(2)

password = 12345
pin = int(input("Enter your PIN: "))
balance = 5000

if pin == password:
    while True:
        print("""
        1 == Balance
        2 == Withdraw
        3 == Deposit
        4 == Exit
        """)
        try:
            option = int(input("Please enter your choice: "))
        except:
            print("Please enter a valid numeric option.")
            continue

        if option == 1:
            print(f"Your current balance is: ₹{balance}")
        
        elif option == 2:
            withdraw_amount = int(input("Please enter withdrawal amount: "))
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"₹{withdraw_amount} has been debited from your account.")
                print(f"Your current balance is ₹{balance}")
            else:
                print("Insufficient balance.")
        
        elif option == 3:
            deposit_amount = int(input("Please enter deposit amount: "))
            balance += deposit_amount
            print(f"₹{deposit_amount} has been credited to your account.")
            print(f"Your updated balance is ₹{balance}")
        
        elif option == 4:
            print("Thank you for using our ATM. Please take your card.")
            break
        
        else:
            print("Invalid option. Please choose between 1 to 4.")
else:
    print("Wrong PIN. Please try again.")
