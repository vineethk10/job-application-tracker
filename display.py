def display_application(application):
    print("-" * 40)
    print(f"Company: {application.get('company', 'N/A')}")
    print(f"Role: {application.get('role', 'N/A')}")
    print(f"Status: {application.get('status', 'N/A')}")
    print(f"Applied Date: {application.get('applied_date', 'N/A')}")
    print(f"Follow-up Date: {application.get('follow_up_date', 'N/A')}")


def display_applications(applications):
    if not applications:
        print("No applications found.")
        return

    for index, application in enumerate(applications, start=1):
        print(f"\nApplication #{index}")
        display_application(application)


def display_summary(summary):
    if not summary:
        print("No applications added yet.")
        return

    print("\nPipeline Summary")
    print("-" * 40)

    for status, count in summary.items():
        print(f"{status}: {count}")

def display_jobs(jobs):
    if not jobs:
        print("No jobs found.")
        return

    for index, job in enumerate(jobs, start=1):
        print(f"\nJob #{index}")
        print("-" * 40)
        print(f"Title: {job.get('title', 'N/A')}")
        print(f"Company: {job.get('company_name', 'N/A')}")
        print(f"Location: {job.get('candidate_required_location', 'N/A')}")
        print(f"Category: {job.get('category', 'N/A')}")
        print(f"URL: {job.get('url', 'N/A')}")