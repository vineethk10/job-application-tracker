from data import load_applications
from utils import show_menu, get_user_input, get_status_choice, get_date_input
from jobs_api import search_latest_jobs
from display import display_applications, display_summary, display_jobs

from tracker import (
    add_application,
    get_all_applications,
    filter_by_status,
    get_pipeline_summary,
    get_pending_followups,
    update_application_status,
    remove_application
)


def main():
    load_applications()
    while True:
        show_menu()

        choice = get_user_input("Choose an option: ")

        if choice == "1":
            company = get_user_input("Company name: ")
            role = get_user_input("Role: ")
            status = get_status_choice()
            applied_date = get_date_input("Applied date MM-DD-YYYY: ")
            follow_up_date = get_date_input(
                "Follow-up date MM-DD-YYYY, optional: ",
                required=False
            )

            add_application(company, role, status, applied_date, follow_up_date)

            print("Application added successfully.")

        elif choice == "2":
            applications = get_all_applications()
            display_applications(applications)

        elif choice == "3":
            status = get_status_choice()
            filtered_applications = filter_by_status(status)
            display_applications(filtered_applications)

        elif choice == "4":
            summary = get_pipeline_summary()
            display_summary(summary)

        elif choice == "5":
            followups = get_pending_followups()
            display_applications(followups)

        elif choice == "6":
            applications = get_all_applications()

            if not applications:
                print("No applications to update.")
                continue

            display_applications(applications)

            application_number = get_user_input("Enter application number to update: ")

            if application_number.isdigit():
                application_index = int(application_number) - 1
                new_status = get_status_choice()

                updated = update_application_status(application_index, new_status)

                if updated:
                    print("Application status updated successfully.")
                else:
                    print("Invalid application number.")
            else:
                print("Please enter a valid number.")

        elif choice == "7":
            applications = get_all_applications()

            if not applications:
                print("No applications to remove.")
                continue

            display_applications(applications)

            application_number = get_user_input("Enter application number to remove: ")

            if application_number.isdigit():
                application_index = int(application_number) - 1
                removed_application = remove_application(application_index)

                if removed_application:
                    print("Application removed successfully.")
                else:
                    print("Invalid application number.")
            else:
                print("Please enter a valid number.")

        elif choice == "8":
            role = get_user_input("Enter job role to search: ")
            jobs = search_latest_jobs(role)
            display_jobs(jobs)

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()