def add_expense(expenses, save_function):
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
    save_function(expenses)

    print("Expense added successfully.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n========== EXPENSES ==========")

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. Amount: ₹{expense['amount']}")
        print(f"   Category: {expense['category']}")
        print(f"   Description: {expense['description']}")
        print("------------------------------")


def search_expenses(expenses):
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


def delete_expense(expenses, save_function):
    if not expenses:
        print("No expenses found.")
        return

    view_expenses(expenses)

    try:
        choice = int(input("Enter choice number to delete: "))
    except ValueError:
        print("Please enter a valid choice.")
        return

    if choice < 1 or choice > len(expenses):
        print("Invalid expense number.")
        return

    deleted_expense = expenses.pop(choice - 1)
    save_function(expenses)

    print(f"Deleted: {deleted_expense['description']}")


def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Spending: ₹{total}")