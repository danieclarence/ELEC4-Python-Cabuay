# Name: Danica A. Cabuay
# Section: IV-BSIT B
# Activity: P3
# Date: November 26, 2026


# Remove extra spaces so "juan   cruz" equals "juan cruz"
def clean_name(name):
    return " ".join(name.split())


def add_student(students, keys, name):
    name = clean_name(name)
    if not name:
        print("Name cannot be empty.")
    elif name.casefold() in keys:  # case-insensitive duplicate check
        print(f"{name} already exists.")
    else:
        students.append(name.title())
        keys.add(name.casefold())
        print(f"{name.title()} added.")


def remove_student(students, keys, name):
    key = clean_name(name).casefold()
    if key not in keys:
        print("Student not found.")
        return
    for student in students:
        if student.casefold() == key:
            students.remove(student)
            keys.remove(key)
            print(f"{student} removed.")
            break