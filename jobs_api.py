import requests


def search_latest_jobs(role, limit=5):
    url = "https://remotive.com/api/remote-jobs"

    params = {
        "search": role
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        jobs = data.get("jobs", [])

        matching_jobs = []

        role_lower = role.lower()

        for job in jobs:
            title = job.get("title", "").lower()
            category = job.get("category", "").lower()
            description = job.get("description", "").lower()

            if (
                role_lower in title
                or role_lower in category
                or role_lower in description
            ):
                matching_jobs.append(job)

        return matching_jobs[:limit]

    except requests.exceptions.RequestException as error:
        print(f"API error: {error}")
        return []