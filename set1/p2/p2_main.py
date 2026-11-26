# Name: Danica A. Cabuay
# Section: IV-BSIT B
# Activity: P2
# Date: November 25, 2026

import student_utils                              # style 1: import module
from student_utils import get_highest, get_lowest  # style 2: from ... import
from datetime import datetime                      # built-in module


# Keep asking until every grade is a number from 0 to 100
def input_grades():
    while True:
        text = input("Enter grades separated by spaces: ")
        try:
            grades = [float(item) for item in text.split()]
        except ValueError:
            print("Numbers only, please.")
            continue
        if grades and all(0 <= g <= 100 for g in grades):
            return grades
        print("Enter at least one grade, each from 0 to 100.")


def main():
    print("=== Student Report by Danica A. Cabuay ===")
    grades = input_grades()
    average = student_utils.compute_average(grades)

    # datetime shows when the report was generated
    now = datetime.now().strftime("%B %d, %Y %I:%M %p")
    print(f"\nReport generated: {now}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {get_highest(grades)}")
    print(f"Lowest : {get_lowest(grades)}")
    print(f"Status : {student_utils.get_status(average)}")


if __name__ == "__main__":
    main()
