# Name: Dan Justin C. Ferrer
# Section: IV-BSIT-B
# Activity: P2 - Custom Module: student_utils
# Date: November 25, 2026


import student_utils
from student_utils import compute_average
from datetime import datetime


def main():
    grades = []

    number = int(input("How many grades will you enter? "))

    for i in range(number):
        grade = float(input("Enter grade: "))
        grades.append(grade)

    print("\n===== STUDENT RESULTS - Dan Justin C. Ferrer =====")
    print("Grades:", grades)
    print("Average:", compute_average(grades))
    print("Highest Grade:", student_utils.get_highest(grades))
    print("Lowest Grade:", student_utils.get_lowest(grades))
    print("Status:", student_utils.get_status(grades))

    print("Report Generated:", datetime.now())


if __name__ == "__main__":
    main()