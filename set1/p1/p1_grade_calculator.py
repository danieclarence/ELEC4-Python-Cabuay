

# Name: Danica A. Cabuay
# Section: IV-BSIT B
# Activity: P1
# Date: November 23, 2026

PASSING_AVERAGE = 75  # global variable


# Ask for one grade until it is a number from 0 to 100
def get_valid_grade(number):
    while True:
        try:
            grade = float(input(f"Enter grade #{number}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if 0 <= grade <= 100:
            return grade
        print("Grade must be from 0 to 100.")


# Accept all of the student's grades
def input_grades():
    while True:
        try:
            count = int(input("How many grades? "))
            if count > 0:
                break
        except ValueError:
            pass
        print("Please enter a whole number greater than 0.")
    return [get_valid_grade(i) for i in range(1, count + 1)]


# Computing functions: they return results and never print
def compute_average(grades):
    total = sum(grades)
    return total / len(grades) if grades else 0


def get_highest(grades):
    return max(grades) if grades else None


def get_lowest(grades):
    return min(grades) if grades else None
