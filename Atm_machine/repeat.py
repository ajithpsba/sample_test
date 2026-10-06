def repeat():
    answer = input("Is the process completed? (yes/no): ")

    if answer == "yes" or answer == "y":
        print("Thank you for using the ATM")
        return False

    elif answer == "no" or answer == "n":
        return True

    else:
        print("Invalid choice")
        return repeat()