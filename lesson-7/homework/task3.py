
from abc import ABC, abstractmethod
import json
import csv
from datetime import datetime

# Task class to represent individual tasks
class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

# Abstract base class for file handling
class FileHandler(ABC):
    @abstractmethod
    def save_tasks(self, tasks, file_path):
        pass

    @abstractmethod
    def load_tasks(self, file_path):
        pass

# CSV file handler implementation
class CSVFileHandler(FileHandler):
    def save_tasks(self, tasks, file_path):
        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])

    def load_tasks(self, file_path):
        tasks = []
        try:
            with open(file_path, mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    task = Task(int(row[0]), row[1], row[2], row[3], row[4])
                    tasks.append(task)
        except FileNotFoundError:
            pass
        return tasks

# JSON file handler implementation
class JSONFileHandler(FileHandler):
    def save_tasks(self, tasks, file_path):
        task_list = []
        for task in tasks:
            task_dict = {
                "task_id": task.task_id,
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date,
                "status": task.status
            }
            task_list.append(task_dict)
        with open(file_path, mode="w") as file:
            json.dump(task_list, file, indent=4)

    def load_tasks(self, file_path):
        tasks = []
        try:
            with open(file_path, mode="r") as file:
                task_list = json.load(file)
                for task_dict in task_list:
                    task = Task(
                        task_dict["task_id"],
                        task_dict["title"],
                        task_dict["description"],
                        task_dict["due_date"],
                        task_dict["status"]
                    )
                    tasks.append(task)
        except FileNotFoundError:
            pass
        return tasks

# To-Do Application class
class ToDoApp:
    def __init__(self, file_handler, file_path):
        self.file_handler = file_handler
        self.file_path = file_path
        self.tasks = self.file_handler.load_tasks(self.file_path)

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(task)

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if due_date:
                    task.due_date = due_date
                if status:
                    task.status = status
                print("Task updated successfully!")
                return
        print(f"No task found with ID {task_id}.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return
        print(f"No task found with ID {task_id}.")

    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print(f"No tasks found with status {status}.")
            return
        print(f"Tasks with status {status}:")
        for task in filtered_tasks:
            print(task)

    def save_tasks(self):
        self.file_handler.save_tasks(self.tasks, self.file_path)
        print("Tasks saved successfully!")

    def load_tasks(self):
        self.tasks = self.file_handler.load_tasks(self.file_path)
        print("Tasks loaded successfully!")

# Menu function
def display_menu():
    print("\nWelcome to the To-Do Application!")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Filter tasks by status")
    print("6. Save tasks")
    print("7. Load tasks")
    print("8. Exit")

# Main function to run the application
def main():
    file_path = "tasks.json"  # Change to "tasks.csv" for CSV format
    file_handler = JSONFileHandler()  # Change to CSVFileHandler() for CSV format
    app = ToDoApp(file_handler, file_path)

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            task_id = int(input("Enter Task ID: "))
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD, optional): ") or None
            status = input("Enter Status (Pending/In Progress/Completed): ")
            task = Task(task_id, title, description, due_date, status)
            app.add_task(task)
        elif choice == "2":
            app.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter Task ID to update: "))
            title = input("Enter new Title (leave blank to skip): ") or None
            description = input("Enter new Description (leave blank to skip): ") or None
            due_date = input("Enter new Due Date (YYYY-MM-DD, leave blank to skip): ") or None
            status = input("Enter new Status (leave blank to skip): ") or None
            app.update_task(task_id, title, description, due_date, status)
        elif choice == "4":
            task_id = int(input("Enter Task ID to delete: "))
            app.delete_task(task_id)
        elif choice == "5":
            status = input("Enter status to filter (Pending/In Progress/Completed): ")
            app.filter_tasks(status)
        elif choice == "6":
            app.save_tasks()
        elif choice == "7":
            app.load_tasks()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()