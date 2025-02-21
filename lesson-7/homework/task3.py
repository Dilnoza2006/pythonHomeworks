import csv
import json
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["task_id"],
            data["title"],
            data["description"],
            data.get("due_date"),
            data.get("status", "Pending")
        )

class StorageInterface:
    def save(self, tasks, filename):
        raise NotImplementedError

    def load(self, filename):
        raise NotImplementedError

class CSVStorage(StorageInterface):
    def save(self, tasks, filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=tasks[0].to_dict().keys())
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())
        print("Tasks saved to CSV successfully!")

    def load(self, filename):
        tasks = []
        try:
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    tasks.append(Task.from_dict(row))
        except FileNotFoundError:
            print("CSV file not found.")
        return tasks

class JSONStorage(StorageInterface):
    def save(self, tasks, filename):
        with open(filename, 'w') as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)
        print("Tasks saved to JSON successfully!")

    def load(self, filename):
        tasks = []
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                tasks = [Task.from_dict(item) for item in data]
        except FileNotFoundError:
            print("JSON file not found.")
        return tasks

class TaskManager:
    def __init__(self, storage: StorageInterface):
        self.tasks = []
        self.storage = storage

    def add_task(self, task: Task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self, status_filter=None):
        for task in self.tasks:
            if status_filter is None or task.status == status_filter:
                print(task)

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = title or task.title
                task.description = description or task.description
                task.due_date = due_date or task.due_date
                task.status = status or task.status
                print("Task updated successfully!")
                return
        print("Task ID not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def save_tasks(self, filename):
        self.storage.save(self.tasks, filename)

    def load_tasks(self, filename):
        self.tasks = self.storage.load(filename)

    def run(self):
        while True:
            print("\n1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                task_id = input("Enter Task ID: ")
                title = input("Enter Title: ")
                description = input("Enter Description: ")
                due_date = input("Enter Due Date (YYYY-MM-DD, optional): ") or None
                status = input("Enter Status (Pending/In Progress/Completed): ") or "Pending"
                self.add_task(Task(task_id, title, description, due_date, status))
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                task_id = input("Enter Task ID to update: ")
                title = input("Enter new Title (leave blank to skip): ") or None
                description = input("Enter new Description (leave blank to skip): ") or None
                due_date = input("Enter new Due Date (YYYY-MM-DD, leave blank to skip): ") or None
                status = input("Enter new Status (Pending/In Progress/Completed, leave blank to skip): ") or None
                self.update_task(task_id, title, description, due_date, status)
            elif choice == "4":
                task_id = input("Enter Task ID to delete: ")
                self.delete_task(task_id)
            elif choice == "5":
                status_filter = input("Enter status to filter by (Pending/In Progress/Completed): ")
                self.view_tasks(status_filter)
            elif choice == "6":
                filename = input("Enter filename to save tasks: ")
                self.save_tasks(filename)
            elif choice == "7":
                filename = input("Enter filename to load tasks: ")
                self.load_tasks(filename)
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    storage_type = input("Choose storage type (csv/json): ").strip().lower()
    storage = CSVStorage() if storage_type == "csv" else JSONStorage()
    manager = TaskManager(storage)
    manager.run()
