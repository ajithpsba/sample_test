from check_balance import balance
def deposit():
    global balance

    amount = float(input("Enter the amount to deposit: "))

    if amount > 0:
        balance += amount
        print(amount,"₹ has been deposited")
        print("New balance: ", balance,"₹")
    else:
        print("Enter a valid amount")