def display_floors():
    
    print("\nAvailable Floors: 0 to 5")
    print("0 - Ground Floor")
    print("1 - First Floor")
    print("2 - Second Floor")
    print("3 - Third Floor")
    print("4 - Fourth Floor")
    print("5 - Fifth Floor")


def move_lift(current_floor, destination):
    if destination > current_floor:
        print("\nLift moving UP...")

        for floor in range(current_floor + 1, destination + 1):
            print(f"Lift is at Floor {floor}")

    elif destination < current_floor:
        print("\nLift moving DOWN...")

        for floor in range(current_floor - 1, destination - 1, -1):
            print(f"Lift is at Floor {floor}")

    else:
        print("\nYou are already on this floor!")

    return destination


def lift_system():
    current_floor = 0

    print("===== WELCOME TO PYTHON LIFT SYSTEM =====")

    while True:
        print(f"\nCurrent Floor: {current_floor}")
        print("1. Select Destination")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_floors()

            try:
                destination = int(input("Enter destination floor: "))

                if 0 <= destination <= 5:
                    current_floor = move_lift(
                        current_floor, destination
                    )
                    print("Lift arrived at destination!")

                else:
                    print("Invalid floor! Choose between 0 and 5.")

            except ValueError:
                print("Please enter a valid floor number.")

        elif choice == "2":
            print("Lift system shutting down. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1 or 2.")