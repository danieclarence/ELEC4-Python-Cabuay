# Name: Danica A. Cabuay
# Section: IV-BSIT B
# Activity: P1
# Date: November 23, 2026

def compute_average(grades):
    total = sum(grades)
    return total / len(grades) if grades else 0

def get_highest(grades):
    return max(grades) if grades else None      

def get_lowest(grades):
    return min(grades) if grades else None