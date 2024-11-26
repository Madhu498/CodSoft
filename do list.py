import json
from datetime import datetime

class Task:
    def __init__(self, title, description="", due_date=None, priority="Low", completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed
        }

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for idx, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Pending"
            print(f"{idx}. {task.title} - {status}")
            print(f"   Description: {task.description}")
            print(f"   Due Date: {task.due_date if task.due_date else 'None'}")
            print(f"   Priority: {task.priority}")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted.")
        else:
            print("Invalid task number.")

    def save_tasks(self, filename='tasks.json'):
        with open(filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f)
        print("Tasks saved.")

    def load_tasks(self, filename='tasks.json'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task(**task_data) for task_data in data]
            print("Tasks loaded.")
        except FileNotFoundError:
            print("No saved tasks found.")

def get_task_input():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
    if due_date:
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date().isoformat()
    priority = input("Enter priority (Low, Medium, High): ")
    return Task(title, description, due_date, priority)

if __name__ == "__main__":
    to_do_list = ToDoList()
    to_do_list.load_tasks()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Save and Exit")

        choice = input("Choose an action: ")

        if choice == "1":
            task = get_task_input()
            to_do_list.add_task(task)
            print("Task added.")
        elif choice == "2":
            to_do_list.view_tasks()
        elif choice == "3":
            to_do_list.view_tasks()
            index = int(input("Enter task number to mark as complete: ")) - 1
            if 0 <= index < len(to_do_list.tasks):
                to_do_list.tasks[index].mark_complete()
                print("Task marked as complete.")
            else:
                print("Invalid task number.")
        elif choice == "4":
            to_do_list.view_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            to_do_list.delete_task(index)
        elif choice == "5":
            to_do_list.save_tasks()
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose a valid action.")
