File name :task.json




todo_lost.py :    import json
import os

FILENAME = "tasks.json"

# Function to load tasks from file
def load_tasks():
    if os.path.exists():
        with open(task.json, "r") as file:
            return json.load(file)
    return []

# Function to save tasks into file
def save_tasks(tasks):
    with open(task.json, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to display all tasks
def view_tasks(tasks):
    if not tasks:
        print("📂 No tasks found.")
    else:
        print("\n📝 Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "❌"
            print(f"{idx}. {task['task']} [{status}]")

# Function to add a task
def add_task(tasks):
    task_name = input("Enter new task: ")
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print("✅ Task added successfully!")

# Function to mark task as done
def mark_done(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as done: "))
        tasks[choice - 1]["done"] = True
        save_tasks(tasks)
        print("🎉 Task marked as completed!")
    except (ValueError, IndexError):
        print("⚠️ Invalid choice.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        deleted = tasks.pop(choice - 1)
        save_tasks(tasks)
        print(f"🗑️ Task '{deleted['task']}' deleted successfully!")
    except (ValueError, IndexError):
        print("⚠️ Invalid choice.")

# Main Program
def todo_app():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please try again.")

# Run the App
todo_app()
