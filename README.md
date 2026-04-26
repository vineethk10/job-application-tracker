# Job Application Tracker

A modular **Python CLI application** to track job applications, manage statuses, and monitor follow-ups. This project demonstrates core Python concepts along with real-world application features like data persistence and API integration.

---

## 🚀 Features

### Core Functionality

* Add job applications
* View all applications
* Update application status
* Remove applications
* Filter applications by status
* View pipeline summary
* Track pending follow-ups

### Data & Validation

* JSON-based data persistence (data saved across sessions)
* Date validation (MM-DD-YYYY format)
* Controlled status selection (predefined options)

### API Integration

* Fetch latest job listings by role using external API
* Display top 5 relevant jobs with company, role, and link

---

## 📁 Project Structure

```text
job_application_tracker/
│
├── main.py        → Application entry point (CLI flow)
├── data.py        → Data storage, JSON load/save, constants
├── tracker.py     → Core business logic (CRUD operations)
├── display.py     → Output formatting and printing
├── utils.py       → Helper functions (input, validation)
├── jobs_api.py    → External API integration for job search
└── applications.json → Stored application data (auto-generated)
```

---

## 🛠️ Tech Stack

* Python
* JSON (for data storage)
* Requests (for API calls)

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install requests
```

2. Run the application:

```bash
python main.py
```

---

## 📌 Sample Use Cases

* Track all job applications in one place
* Monitor interview pipeline
* Keep follow-up reminders
* Explore new job opportunities via API

---

## 🧠 Concepts Covered

* Modular programming
* Functions and control flow
* Lists and dictionaries
* File handling (JSON)
* Input validation
* Date handling (`datetime`)
* API integration (`requests`)
* CLI application design

---

## 🔮 Future Improvements

* Add notes and recruiter contact info
* Advanced follow-up reminders (overdue/today/upcoming)
* Analytics dashboard (conversion rates)
* Export data to CSV
* OOP refactor
* Web UI using Flask or FastAPI
* Database integration (SQLite/PostgreSQL)

---

## 📄 License

This project is for learning and personal use.

---

## 🙌 Acknowledgment

Built as part of a Python learning journey to practice real-world problem solving and application design.