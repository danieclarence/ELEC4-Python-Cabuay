# Name: Danica A. Cabuay
# Section: IV-BSIT B
# Activity: P4
# Date: November 26, 2026


def divide_numbers():
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))
        result = first / second
    except ValueError:
        print("Error: please enter numbers only.")
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")
    else:
        # runs only when there is no error
        print(f"Result: {result}")
    finally:
        # always runs
        print("Division finished.")
