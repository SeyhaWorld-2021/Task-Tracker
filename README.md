#  Task Tracker CLI

A lightweight **command-line task tracker** built with Python.  
Manage your tasks easily by adding, updating, deleting, and tracking their status with a simple JSON file.  

No external libraries. Pure Python. Beginner-friendly and extendable.

---

##  Features

- Add new tasks
- Update task status (`todo`, `in-progress`, `done`)
- Delete tasks
- List all tasks
- Filter tasks by status
- Colored CLI output using ANSI codes
- Tasks stored locally in a JSON file

---

##  Project Structure

```text
task-tracker-cli/
│── task.py          # Main CLI application
│── tasks.json       # Task storage (auto-created, gitignored)
│── images/          # Optional: screenshots
│   └── preview.png
│── .gitignore
│── README.md
