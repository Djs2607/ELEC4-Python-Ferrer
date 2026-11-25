# Name: Dan Justin C. Ferrer
# Section: IV-BSIT-B
# Activity: P1 - Student Grade Calculator
# Date: November 16, 2026

PASSING_GRADE = 75  


def enter_grades():
    grades = []

    while True:
        try:
            number = int(input("How many grades will you enter? "))
            if number > 0:
                break
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    for i in range(number):
        while True:
            try:
                grade = float(input("Enter grade: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be from 0 to 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    return grades


def compute_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def get_status(grades):
    if compute_average(grades) >= PASSING_GRADE:
        return "PASSED"
    else:
        return "FAILED"


def main():
    grades = []

    while True:
        print("\n===== STUDENT GRADE CALCULATOR - Dan Justin C. Ferrer =====")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            grades = enter_grades()

        elif choice == "2":
            if len(grades) == 0:
                print("No grades entered yet.")
            else:
                print("\n===== STUDENT RESULTS - Dan Justin C. Ferrer =====")
                print("Grades:", grades)
                print("Average:", compute_average(grades))
                print("Highest Grade:", get_highest(grades))
                print("Lowest Grade:", get_lowest(grades))
                print("Status:", get_status(grades))

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# Local and Global Variables:
# A global variable is declared outside a function and can be accessed by functions in the program.
# In this program, PASSING_GRADE is a global variable used in get_status() to check if the average is passing.
# A local variable is declared inside a function and can only be accessed within that function.
# For example, grades inside enter_grades() is a local variable because it is created and used within that function.
# The main difference is that a global variable can be accessed by any function in the program, while a local variable can only be used inside the function where it was created.