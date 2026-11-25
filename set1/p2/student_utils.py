# Name: Danica A. Cabuay
# Section: IV-BSIT B
# Activity: P2
# Date: November 25, 2026

# Reusable functions for student grades

PASSING_AVERAGE = 75


def compute_average(grades):
    return sum(grades) / len(grades) if grades else 0


def get_status(average):
    return "PASSED" if average >= PASSING_AVERAGE else "FAILED"


def get_highest(grades):
    return max(grades) if grades else None


def get_lowest(grades):
    return min(grades) if grades else None


# Runs only when this file is executed directly, not when imported
if __name__ == "__main__":
    print("This is a module. Run p2_main.py instead.")