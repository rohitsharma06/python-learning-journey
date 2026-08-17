import json


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


expenses = load_expenses()


def add_expense():
    while True:
        try:
            amount = int(input("Enter your Expense Amount: "))
            break
        except ValueError:
            print("Please enter a valid amount.")

    category = input("Enter category: ").title()
    description = input("Enter expense description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully.")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n========== EXPENSES ==========")

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. Amount: ₹{expense['amount']}")
        print(f"   Category: {expense['category']}")
        print(f"   Description: {expense['description']}")
        print("------------------------------")


def search_expenses():
    category = input("Enter category to search: ").strip().lower()

    found = False

    for expense in expenses:
        if expense["category"].lower() == category:
            print(f"Amount: ₹{expense['amount']}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")
            print("------------------------------")
            found = True

    if not found:
        print("No expenses found for that category.")


def delete_expenses():
    if not expenses:
        print("No expenses found.")
        return

    view_expenses()

    try:
        choice = int(input("Enter choice number to delete: "))
    except ValueError:
        print("Please enter a valid choice.")
        return

    if choice < 1 or choice > len(expenses):
        print("Invalid expense number.")
        return

    deleted_expense = expenses.pop(choice - 1)
    save_expenses()

    print(f"Deleted: {deleted_expense['description']}")


def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Spending: ₹{total}")


def show_menu():
    print("\n========== EXPENSE MANAGER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Delete Expense")
    print("5. Search Expenses")
    print("6. Exit")
    print("=====================================")


while True:
    show_menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_expenses()

    elif choice == 3:
        calculate_total()

    elif choice == 4:
        delete_expenses()

    elif choice == 5:
        search_expenses()

    elif choice == 6:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")