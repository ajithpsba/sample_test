def pin_number():

    while True:

        pin = input("Enter your pin number: ")

        if pin == "7888":
            print("Pin accepted")
            return True

        else:
            print("Pin not accepted")
            print("Please try again")