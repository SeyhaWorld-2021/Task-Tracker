 
#  Task Tracker CLI
##  Preview

<p align="center">
  <img src="image/tasks tracker.PNG" alt="Task Tracker CLI Preview">
</p>

A simple and lightweight **command-line task tracker** built with Python.  
This project helps you manage tasks by adding, updating, deleting, and tracking their status using a local JSON file.

No external libraries. No frameworks. Just clean Python and CLI fundamentals.

---

##  Features

- Add new tasks
- Update task status (`todo`, `in-progress`, `done`)
- Delete tasks
- List all tasks
- Filter tasks by status
- Colored CLI output using ANSI escape codes
- Tasks stored locally in a JSON file
- Beginner-friendly and easy to extend

---

##  Project Structure

```text
task-tracker-cli/
│── task.py          # Main CLI application
│── tasks.json       # Task storage (auto-created, gitignored)
│── .gitignore
│── README.md
