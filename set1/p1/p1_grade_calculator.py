

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

def get_status(average):
    return "PASSED" if average >= PASSING_AVERAGE else "FAILED"


def view_results(grades):
    if not grades:
        print("No grades yet. Choose option 1 first.")
        return
    average = compute_average(grades)
    print(f"Grades : {grades}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {get_highest(grades)}")
    print(f"Lowest : {get_lowest(grades)}")
    print(f"Status : {get_status(average)}")


def main():
    grades = []  # local variable
    while True:
        print("\n=== Grade Calculator by Danica A. Cabuay ===")
        print("1. Enter grades")
        print("2. View results")
        print("3. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            grades = input_grades()
        elif choice == "2":
            view_results(grades)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 3.")


if _name_ == "_main_":
    main()

# Local vs global: PASSING_AVERAGE is a global variable because it is declared
# outside all functions, so get_status() can read it. The grades variable inside
# main() is local, so it only exists within main(). Other functions can use the
# grades only when main() passes them as a parameter.