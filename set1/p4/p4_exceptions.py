
# Name: Dan Justin C. Ferrer
# Section: IV-BSIT-B
# Activity: P4 - Safe Menu Program
# Date: November 26, 2026


def division():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2

    except ValueError:
        print("Invalid input. Please enter numbers.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    else:
        print("Result:", result)

    finally:
        print("Division operation completed.")


def open_file():
    try:
        filename = input("Enter file name: ")

        file = open(filename, "r")
        content = file.read()
        file.close()

    except FileNotFoundError:
        print("File not found.")

    else:
        print("\n===== FILE CONTENTS =====")
        print(content)

    finally:
        print("File operation completed.")


def main():
    while True:
        print("\n===== SAFE MENU PROGRAM  - Dan Justin C. Ferrer =====")
        print("1. Division")
        print("2. Open File")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            division()

        elif choice == "2":
            open_file()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid menu selection. Please try again.")


if __name__ == "__main__":
    main()
