import json
import os

# Account class to represent individual accounts
class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: ${self.balance:.2f}"

# Bank class to manage all accounts and operations
class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return
        account_number = self._generate_account_number()
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print(f"Account with number {account_number} not found.")

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        account = self.accounts.get(account_number)
        if account:
            account.balance += amount
            self.save_to_file()
            print(f"Deposited ${amount:.2f}. New balance: ${account.balance:.2f}")
        else:
            print(f"Account with number {account_number} not found.")

    def withdraw(self, account_number, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        account = self.accounts.get(account_number)
        if account:
            if amount > account.balance:
                print("Insufficient funds.")
            else:
                account.balance -= amount
                self.save_to_file()
                print(f"Withdrew ${amount:.2f}. New balance: ${account.balance:.2f}")
        else:
            print(f"Account with number {account_number} not found.")

    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            accounts_data = {
                acc_num: {"name": acc.name, "balance": acc.balance}
                for acc_num, acc in self.accounts.items()
            }
            json.dump(accounts_data, file)

    def load_from_file(self):
        if os.path.exists("accounts.txt"):
            with open("accounts.txt", "r") as file:
                accounts_data = json.load(file)
                for acc_num, data in accounts_data.items():
                    self.accounts[acc_num] = Account(acc_num, data["name"], data["balance"])

    def _generate_account_number(self):
        return str(len(self.accounts) + 1)

# Menu function
def display_menu():
    print("\nWelcome to the Bank Application!")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

# Main function to run the application
def main():
    bank = Bank()

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(name, initial_deposit)
        elif choice == "2":
            account_number = input("Enter account number: ")
            bank.view_account(account_number)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)
        elif choice == "4":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)
        elif choice == "5":
            print("Thank you for using the Bank Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()