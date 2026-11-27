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


def open_file():
    file_name = input("File name: ").strip()
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: file not found.")
    except (OSError, UnicodeDecodeError):
        print("Error: that file cannot be read.")
    else:
        print("--- File contents ---")
        print(content)
    finally:
        print("File operation finished.")


def main():
    while True:
        print("\n=== Safe Menu by Danica A. Cabuay ===")
        print("1. Divide  2. Open file  3. Exit")
        try:
            choice = int(input("Choose: "))
        except ValueError:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        if choice == 1:
            divide_numbers()
        elif choice == 2:
            open_file()
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if _name_ == "_main_":
    main()
