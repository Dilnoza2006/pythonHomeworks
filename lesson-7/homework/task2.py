import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    @staticmethod
    def from_string(data_str):
        employee_id, name, position, salary = data_str.strip().split(", ")
        return Employee(employee_id, name, position, float(salary))


class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'w') as f:
                pass

    def add_employee(self, employee: Employee):
        if self.get_employee_by_id(employee.employee_id):
            print("Error: Employee ID must be unique.")
            return
        with open(self.FILE_NAME, 'a') as f:
            f.write(str(employee) + "\n")
        print("Employee added successfully!")

    def view_all_employees(self, sort_by=None):
        employees = self._load_employees()
        if sort_by == "name":
            employees.sort(key=lambda e: e.name)
        elif sort_by == "salary":
            employees.sort(key=lambda e: e.salary)
        print("Employee Records:")
        for emp in employees:
            print(emp)

    def get_employee_by_id(self, employee_id):
        employees = self._load_employees()
        for emp in employees:
            if emp.employee_id == employee_id:
                return emp
        return None

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        employees = self._load_employees()
        updated = False
        with open(self.FILE_NAME, 'w') as f:
            for emp in employees:
                if emp.employee_id == employee_id:
                    if name:
                        emp.name = name
                    if position:
                        emp.position = position
                    if salary:
                        emp.salary = salary
                    updated = True
                f.write(str(emp) + "\n")
        if updated:
            print("Employee updated successfully!")
        else:
            print("Employee ID not found.")

    def delete_employee(self, employee_id):
        employees = self._load_employees()
        employees = [emp for emp in employees if emp.employee_id != employee_id]
        with open(self.FILE_NAME, 'w') as f:
            for emp in employees:
                f.write(str(emp) + "\n")
        print("Employee deleted successfully!")

    def _load_employees(self):
        employees = []
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'r') as f:
                for line in f:
                    if line.strip():
                        employees.append(Employee.from_string(line))
        return employees

    def run(self):
        while True:
            print("\n1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                employee_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = float(input("Enter Salary: "))
                self.add_employee(Employee(employee_id, name, position, salary))
            elif choice == "2":
                sort_by = input("Sort by 'name' or 'salary' (leave blank for no sorting): ").strip()
                self.view_all_employees(sort_by if sort_by in ["name", "salary"] else None)
            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ")
                emp = self.get_employee_by_id(employee_id)
                if emp:
                    print("Employee Found:")
                    print(emp)
                else:
                    print("Employee ID not found.")
            elif choice == "4":
                employee_id = input("Enter Employee ID to update: ")
                name = input("Enter new Name (leave blank to skip): ") or None
                position = input("Enter new Position (leave blank to skip): ") or None
                salary = input("Enter new Salary (leave blank to skip): ")
                salary = float(salary) if salary else None
                self.update_employee(employee_id, name, position, salary)
            elif choice == "5":
                employee_id = input("Enter Employee ID to delete: ")
                self.delete_employee(employee_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Example usage
if __name__ == '__main__':
    manager = EmployeeManager()
    manager.run()
