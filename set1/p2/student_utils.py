# Name: Dan Justin C. Ferrer
# Section: IV-BSIT-B
# Activity: P2 - Custom Module: student_utils
# Date: November 25, 2026


PASSING_GRADE = 75

def compute_average(grades):
    return sum(grades) / len(grades)


def get_status(grades):
    if compute_average(grades) >= PASSING_GRADE:
        return "PASSED"
    else:
        return "FAILED"


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)