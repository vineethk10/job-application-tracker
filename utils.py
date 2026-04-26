from datetime import datetime
from data import STATUSES

def show_menu():
    print("\nJob Application Tracker")
    print("1. Add application")
    print("2. View all applications")
    print("3. Filter by status")
    print("4. View pipeline summary")
    print("5. View pending follow-ups")
    print("6. Update application status")
    print("7. Remove application")
    print("8. Search latest jobs by role")
    print("9. Exit")

def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, "%m-%d-%Y")
        return True
    except ValueError:
        return False

def get_user_input(prompt):
    return input(prompt).strip()

def show_status_options():
    print("\nSelect status:")

    for index, status in enumerate(STATUSES, start=1):
        print(f"{index}. {status}")

def get_status_choice():
    while True:
        show_status_options()
        choice = get_user_input("Choose a status: ")

        if choice.isdigit():
            index = int(choice)

            if 1 <= index <= len(STATUSES):
                return STATUSES[index - 1]

        print("Invalid status. Please try again.")

def get_date_input(prompt, required=True):
    while True:
        date_text = input(prompt).strip()

        if not date_text and not required:
            return ""

        if is_valid_date(date_text):
            return date_text

        print("Invalid date format. Please use MM-DD-YYYY.")