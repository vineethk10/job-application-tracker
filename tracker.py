from data import applications, save_applications


def add_application(company, role, status, applied_date, follow_up_date):
    application = {
        "company": company,
        "role": role,
        "status": status,
        "applied_date": applied_date,
        "follow_up_date": follow_up_date
    }

    applications.append(application)
    save_applications()

    return application


def get_all_applications():
    return applications


def filter_by_status(status):
    result = []

    for application in applications:
        if application["status"].lower() == status.lower():
            result.append(application)

    return result


def get_pipeline_summary():
    summary = {}

    for application in applications:
        status = application["status"]

        if status in summary:
            summary[status] += 1
        else:
            summary[status] = 1

    return summary


def get_pending_followups():
    result = []

    for application in applications:
        if application["follow_up_date"]:
            result.append(application)

    return result


def update_application_status(application_index, new_status):
    if 0 <= application_index < len(applications):
        applications[application_index]["status"] = new_status
        save_applications()
        return True

    return False


def remove_application(application_index):
    if 0 <= application_index < len(applications):
        removed_application = applications.pop(application_index)
        save_applications()
        return removed_application

    return None