# ATM-simulation
This Python script simulates the basic functionalities of an ATM (Automated Teller Machine). It provides a user-friendly interface through the console where the user can interact by entering their PIN and performing common banking operations such as checking balance, withdrawing money, depositing money, or exiting the session.
Key Features and Functionality:
Card Insertion Simulation:

The program begins by printing "Please insert your card" and waits for 2 seconds using time.sleep(2) to simulate the card reading delay.

PIN Authentication:

A pre-defined PIN (12345) is used as a simple security check.

The user is prompted to enter their PIN.

If the entered PIN matches the stored one, access is granted; otherwise, an error message is displayed: "Wrong PIN. Please try again.".

Main Menu (Looping Interface):

Once the PIN is correct, the program enters a while True loop that continuously shows the user a menu with 4 options:


1 == Balance
2 == Withdraw
3 == Deposit
4 == Exit
Option Handling:

Option 1 – Balance:
Displays the current account balance.

Option 2 – Withdraw:
Prompts the user to enter the amount to withdraw.
Checks if sufficient balance is available before deducting.
If the balance is insufficient, it shows an error message.

Option 3 – Deposit:
Prompts the user to enter an amount to deposit and adds it to the balance.

Option 4 – Exit:
Ends the session with a goodbye message.

Error Handling:

The program uses a try-except block to handle non-numeric input for menu choices.

Invalid options outside the range 1–4 are also handled gracefully.

 Educational Concepts Used:
Input/Output operations

Conditional statements (if, elif, else)

Loops (while True)

Exception handling with try-except

Variable manipulation and arithmetic

Basic user interface with multi-line string menu

 Use Case:
This program is a good example for beginners learning Python who want to practice control structures and simulate real-world systems like ATM operations. It could also be enhanced with additional features like:

PIN retry limit

Transaction history (mini statement)

Account holder details

Multi-user support with dictionary data

