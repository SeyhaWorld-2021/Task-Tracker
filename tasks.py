import json 
import os
import sys

args = sys.argv

FILE_NAME = "tasks.json"

BLUE    = "\033[94m"
RESET   = "\033[0m"
BOLD    = "\033[1m"

def show_banner():
    
    print(f"""{BLUE}{BOLD}
          
████████╗ █████╗ ███████╗██╗  ██╗    ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██║   ███████║███████╗█████╔╝        ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
   ██║   ██╔══██║╚════██║██╔═██╗        ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ██║  ██║███████║██║  ██╗       ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                              {RESET}""")

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)
def add_task(title):
    tasks = load_tasks()
    task_id = tasks[-1]["id"] + 1 if tasks else 1
    
    new_task = {
        "id": task_id,
        "title": title,
        "status": "todo"
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added (ID: {task_id})")
    
def list_tasks(filter_status=None):
    tasks = load_tasks()
    
    if not tasks:
        print("No Tasks Found.")
        return
    for task in tasks:
        if filter_status and task["status"] != filter_status:
            continue
        print(f"[{task['id']}] {task['title']} - {task['status']}")
    
def update_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            save_tasks(tasks)
            print("Task updated.")
            return
    print("Task not found.")
        
def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    
    if len(tasks) == len(new_tasks):
        print("Task not found.")
        return
    
    save_tasks(new_tasks)
    print("Task deleted.")

def main():
    if len(sys.argv) < 2:
        show_banner()
        print("Usage: python tasks.py <command>")
        return
    
    command = sys.argv[1]
    
    if command == "add":
        add_task(sys.argv[2])
        
    elif command == "list":
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
            
    elif command == "done":
        update_status(int(sys.argv[2]), "done")
        
    elif command == "progress":
        update_status(int(sys.argv[2]), "in-progress")
        
    elif command == "delete":
        delete_task(int(sys.argv[2]))
        
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()


















