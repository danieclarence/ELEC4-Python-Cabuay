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

def search_student(students, text):
    text = clean_name(text).casefold()




    if not text:
        print("Search text cannot be empty.")
        return
    # partial match: "cruz" finds "Juan Cruz"
    matches = [s for s in students if text in s.casefold()]
    if matches:
        for student in sorted(matches):
            print(f"Found: {student}")
    else:
        print("No match found.")


def display_students(students):
    if not students:
        print("No students yet.")
    for number, student in enumerate(sorted(students), start=1):
        print(f"{number}. {student}")
    print(f"Total: {len(students)}")


def main():
    students = []  # list: holds the names
    keys = set()   # set: holds lowercase names to block duplicates

    while True:
        print("\n=== Record Manager by Danica A. Cabuay ===")
        print("1. Add  2. Remove  3. Search  4. Display  5. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_student(students, keys, input("Name to add: "))
        elif choice == "2":
            remove_student(students, keys, input("Name to remove: "))
        elif choice == "3":
            search_student(students, input("Search: "))
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()

# List vs set: A list keeps items in order and allows duplicates, while a set is
# unordered and stores only unique items. I used the list (students) to hold,
# sort, and display the names. I used the set (keys) to store lowercase names so
# duplicates can be checked quickly.