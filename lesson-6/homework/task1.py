import os

def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Employee record added successfully!\n")

def view_employees():
    if not os.path.exists("employees.txt"):
        print("No records found.\n")
        return
    with open("employees.txt", "r") as file:
        records = file.readlines()
        if not records:
            print("No records found.\n")
        else:
            for record in records:
                print(record.strip())

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    with open("employees.txt", "r") as file:
        for line in file:
            if line.startswith(emp_id + ","):
                print("Employee Found:", line.strip())
                return
    print("Employee not found.\n")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated_records = []
    found = False
    with open("employees.txt", "r") as file:
        for line in file:
            if line.startswith(emp_id + ","):
                found = True
                name = input("Enter New Name: ")
                position = input("Enter New Position: ")
                salary = input("Enter New Salary: ")
                updated_records.append(f"{emp_id}, {name}, {position}, {salary}\n")
            else:
                updated_records.append(line)
    if found:
        with open("employees.txt", "w") as file:
            file.writelines(updated_records)
        print("Employee record updated successfully!\n")
    else:
        print("Employee not found.\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    updated_records = []
    found = False
    with open("employees.txt", "r") as file:
        for line in file:
            if line.startswith(emp_id + ","):
                found = True
            else:
                updated_records.append(line)
    if found:
        with open("employees.txt", "w") as file:
            file.writelines(updated_records)
        print("Employee record deleted successfully!\n")
    else:
        print("Employee not found.\n")

def main():
    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
