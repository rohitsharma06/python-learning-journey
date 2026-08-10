from datetime import datetime


def load_expenses():

    expenses = []

    try:
        file = open("expenses.txt", "r")

        for line in file:

            expense_id, amount, description, category, date = line.strip().split(",")

            expense = {
                "id": int(expense_id),
                "amount": float(amount),
                "description": description,
                "category": category,
                "date": date
            }

            expenses.append(expense)

        file.close()

    except FileNotFoundError:
        pass

    return expenses


def save_expenses(expenses):

    file = open("expenses.txt", "w")

    for expense in expenses:

        file.write(
            f"{expense['id']},"
            f"{expense['amount']},"
            f"{expense['description']},"
            f"{expense['category']},"
            f"{expense['date']}\n"
        )

    file.close()


def show_menu():

    print("========== EXPENSE TRACKER ==========")
    print("1. View Expenses")
    print("2. Add Expense")
    print("3. Delete Expense")
    print("4. Total Expenses")
    print("5. Category Summary")
    print("6. Exit")
    print("=====================================")


def view_expenses(expenses):

    if len(expenses) == 0:
        print("No expenses available.")
        return

    print("\n---------- Your Expenses ----------")

    for expense in expenses:

        print("----------------------------")
        print(f"Expense ID: {expense['id']}")
        print(f"Amount    : ₹{expense['amount']:.2f}")
        print(f"Details   : {expense['description']}")
        print(f"Category  : {expense['category']}")
        print(f"Date      : {expense['date']}")

    print("----------------------------")


def add_expense(expenses):

    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    description = input("Enter expense description: ").strip().title()

    if description == "":
        print("Description cannot be empty.")
        return

    category = input("Enter expense category: ").strip().title()

    if category == "":
        print("Category cannot be empty.")
        return

    date = datetime.now().strftime("%d-%m-%Y")

    if len(expenses) == 0:
        expense_id = 1
    else:
        expense_id = expenses[-1]["id"] + 1

    expense = {
        "id": expense_id,
        "amount": amount,
        "description": description,
        "category": category,
        "date": date
    }

    expenses.append(expense)

    save_expenses(expenses)

    print("Expense added successfully.")


def delete_expense(expenses):

    if len(expenses) == 0:
        print("No expenses available to delete.")
        return

    try:
        expense_id = int(input("Enter expense ID to delete: "))
    except ValueError:
        print("Please enter numbers only.")
        return

    for expense in expenses:

        if expense["id"] == expense_id:

            expenses.remove(expense)

            save_expenses(expenses)

            print(
                f"₹{expense['amount']:.2f} "
                f"({expense['description']}) deleted successfully."
            )

            return

    print("Expense not found.")


def total_expenses(expenses):

    if len(expenses) == 0:
        print("No expenses available.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total Expenses: ₹{total:.2f}")


def category_summary(expenses):

    if len(expenses) == 0:
        print("No expenses available.")
        return

    category_totals = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\n---------- Category Summary ----------")

    for category in category_totals:
        print(f"{category}: ₹{category_totals[category]:.2f}")

    print("--------------------------------------")


expenses = load_expenses()


while True:

    show_menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter numbers only.")
        continue

    if choice < 1 or choice > 6:
        print("Please enter a number between 1 and 6.")
        continue

    if choice == 1:
        view_expenses(expenses)

    elif choice == 2:
        add_expense(expenses)

    elif choice == 3:
        delete_expense(expenses)

    elif choice == 4:
        total_expenses(expenses)

    elif choice == 5:
        category_summary(expenses)

    elif choice == 6:
        print("Thank You For Using Expense Tracker")
        break