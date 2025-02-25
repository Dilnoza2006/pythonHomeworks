import csv
import json

# Load tasks from JSON file
def load_tasks(file_path='tasks.json'):
    with open(file_path, 'r') as file:
        tasks = json.load(file)
    return tasks

# Display all tasks
def display_tasks(tasks):
    print("ID\tTask Name\tCompleted\tPriority")
    for task in tasks:
        print(f"{task['id']}\t{task['task']}\t{task['completed']}\t{task['priority']}")

# Save tasks to JSON file
def save_tasks(tasks, file_path='tasks.json'):
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"Tasks saved to {file_path}")

# Calculate task completion statistics
def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = len([t for t in tasks if t['completed']])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(t['priority'] for t in tasks) / total_tasks if total_tasks > 0 else 0
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

# Convert tasks to CSV
def convert_to_csv(tasks, file_path='tasks.csv'):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Task', 'Completed', 'Priority'])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])
    print(f"Tasks converted to CSV at {file_path}")

if __name__ == '__main__':
    tasks = load_tasks()
    display_tasks(tasks)
    calculate_stats(tasks)
    convert_to_csv(tasks)
    save_tasks(tasks)
