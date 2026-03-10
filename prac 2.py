def print_state(x, y):
    print(f"Jug 1: {x} liters, Jug 2: {y} liters")


def main():
    c1 = int(input("Enter the capacity of the first jug: "))
    c2 = int(input("Enter the capacity of the second jug: "))
    t1 = int(input("Enter the target amount of water in the first jug: "))
    t2 = int(input("Enter the target amount of water in the second jug: "))

    x, y = 0, 0

    while True:
        print_state(x, y)

        if x == t1 and y == t2:
            print("Target reached!")
            break

        print("\nChoose an action:")
        print("1: Fill Jug 1")
        print("2: Fill Jug 2")
        print("3: Empty Jug 1")
        print("4: Empty Jug 2")
        print("5: Pour Jug 1 into Jug 2")
        print("6: Pour Jug 2 into Jug 1")
        print("7: Exit")

        choice = int(input("Enter your choice (1-7): "))

        if choice == 1:
            x = c1

        elif choice == 2:
            y = c2

        elif choice == 3:
            x = 0

        elif choice == 4:
            y = 0

        elif choice == 5:
            transfer = min(x, c2 - y)
            x -= transfer
            y += transfer

        elif choice == 6:
            transfer = min(y, c1 - x)
            y -= transfer
            x += transfer

        elif choice == 7:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()