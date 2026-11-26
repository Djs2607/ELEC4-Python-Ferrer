
# Name: Dan Justin C. Ferrer
# Section: IV-BSIT-B
# Activity: P3 - Student Record Manager
# Date: November 26, 2026


students = []
student_set = set()


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Please enter a valid name.")
    elif name.lower() in student_set:
        print("Student already exists.")
    else:
        students.append(name)
        student_set.add(name.lower())
        print("Student added successfully.")


def remove_student():
    name = input("Enter student name to remove: ").strip()

    if name.lower() in student_set:
        student_set.remove(name.lower())

        for student in students:
            if student.lower() == name.lower():
                students.remove(student)
                break

        print("Student removed successfully.")
    else:
        print("Student not found.")


def search_student():
    name = input("Enter name to search: ").strip()

    found = False

    for student in students:
        if name.lower() in student.lower():
            print(student)
            found = True

    if not found:
        print("Student not found.")


def display_students():
    if len(students) == 0:
        print("No students found.")
    else:
        print("\n===== STUDENT LIST  - Dan Justin C. Ferrer =====")

        sorted_students = sorted(students, key=str.lower)

        for i, student in enumerate(sorted_students, start=1):
            print(f"{i}. {student}")

        print("Total Students:", len(students))


def main():
    while True:
        print("\n===== STUDENT RECORD MANAGER - Dan Justin C. Ferrer =====")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            remove_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            display_students()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# Difference between List and Set:
# A list is an ordered collection that allows duplicate values.
# A set is an unordered collection that stores unique values only.
# In this program, I used a list to store and display student names.
# I used a set to prevent duplicate student names.
# Both are used to manage the student records efficiently.
