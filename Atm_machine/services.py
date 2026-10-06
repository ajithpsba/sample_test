from deposit import deposit
from withdraw import withdraw
from check_balance import check_balance
from atm_pin import pin_number
from repeat import repeat

def services():

    print("Welcome to the ATM machine")
    print("Please enter your card")

    card = input("Press Enter to continue or type yes: ")

    if card == "" or card == "yes" or card == "y" or card == "Yes" or card == "Y":

        if pin_number():

            print("Card accepted")

            while True:

                print("\nPlease select a service")
                print("1. Check balance")
                print("2. Deposit")
                print("3. Withdraw")

                service = input("Enter your choice: ")

                if service in ["1", "check balance", "balance" , "b", "Check balance", "Balance", "B"]:
                    check_balance()

                elif service in ["2", "deposit", "d" , "Deposit", "D" ]:
                    deposit()

                elif service in ["3", "withdraw", "w" , "Withdraw", "W"]:
                    withdraw()

                else:
                    print("Invalid choice")
                    continue

                if repeat() == False:
                    break

    else:
        print("Card not accepted")


services()