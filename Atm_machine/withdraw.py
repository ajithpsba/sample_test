from check_balance import balance
def withdraw():
    global balance

    amount = float(input("Enter the amount to withdraw: "))

    if amount <= 0:
        print("Enter a valid amount")
    elif amount <= balance:
        balance -= amount
        print("₹", amount, "has been withdrawn")
        print("Remaining balance: ₹", balance)
    else:
        print("Insufficient balance")