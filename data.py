import json
import os

FILE_NAME = "applications.json"

applications = []

STATUSES = ["Applied", "Interview", "Offer", "Rejected", "Follow-up"]


def load_applications():
    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r") as file:
        loaded_applications = json.load(file)

    applications.clear()
    applications.extend(loaded_applications)


def save_applications():
    with open(FILE_NAME, "w") as file:
        json.dump(applications, file, indent=4)