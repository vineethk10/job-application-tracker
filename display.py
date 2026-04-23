def print_application(app):
    print(f"Company: {app['company']}")
    print(f"Role: {app['role']}")
    print(f"Date Applied: {app['date_applied']}")
    print(f"Status: {app['status']}")
    print(f"Follow Up Needed: {app['follow_up']}")
    print("-" * 30)


def print_applications(applications):
    if not applications:
        print("No applications found.")
        return

    for app in applications:
        print_application(app)