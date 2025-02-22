import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    def __init__(self, file_path="employees.txt"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                file.write("")

    def add_employee(self, employee):
        with open(self.file_path, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        if os.path.getsize(self.file_path) == 0:
            print("No employee records found.")
            return
        with open(self.file_path, "r") as file:
            print("Employee Records:")
            for line in file:
                print(line.strip())

    def search_employee(self, employee_id):
        with open(self.file_path, "r") as file:
            for line in file:
                if line.startswith(str(employee_id) + ","):
                    print("Employee Found:")
                    print(line.strip())
                    return
        print(f"No employee found with ID {employee_id}.")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        updated_employees = []
        found = False
        with open(self.file_path, "r") as file:
            for line in file:
                if line.startswith(str(employee_id) + ","):
                    found = True
                    employee_data = line.strip().split(", ")
                    if name:
                        employee_data[1] = name
                    if position:
                        employee_data[2] = position
                    if salary:
                        employee_data[3] = salary
                    updated_employees.append(", ".join(employee_data) + "\n")
                else:
                    updated_employees.append(line)
        if not found:
            print(f"No employee found with ID {employee_id}.")
            return
        with open(self.file_path, "w") as file:
            file.writelines(updated_employees)
        print("Employee updated successfully!")

    def delete_employee(self, employee_id):
        updated_employees = []
        found = False
        with open(self.file_path, "r") as file:
            for line in file:
                if not line.startswith(str(employee_id) + ","):
                    updated_employees.append(line)
                else:
                    found = True
        if not found:
            print(f"No employee found with ID {employee_id}.")
            return
        with open(self.file_path, "w") as file:
            file.writelines(updated_employees)
        print("Employee deleted successfully!")

def display_menu():
    print("\nWelcome to the Employee Records Manager!")
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")

def main():
    manager = EmployeeManager()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            employee = Employee(employee_id, name, position, salary)
            manager.add_employee(employee)
        elif choice == "2":
            manager.view_all_employees()
        elif choice == "3":
            employee_id = input("Enter Employee ID to search: ")
            manager.search_employee(employee_id)
        elif choice == "4":
            employee_id = input("Enter Employee ID to update: ")
            name = input("Enter new Name (leave blank to skip): ")
            position = input("Enter new Position (leave blank to skip): ")
            salary = input("Enter new Salary (leave blank to skip): ")
            manager.update_employee(employee_id, name or None, position or None, salary or None)
        elif choice == "5":
            employee_id = input("Enter Employee ID to delete: ")
            manager.delete_employee(employee_id)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
