from datetime import  datetime

expenses = []

next_expense_id = 1
def show_menu():
    print("========== EXPENSE TRACKER ==========")
    print("1. View Expenses")
    print("2. Add Expense")
    print("3. Delete Expense")
    print("4. Total Expenses")
    print("5. Category Summary")
    print("6. Exit")
    print("=====================================")

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
    # strip use to remove space and title us to capitalize first letter capital

    if description == "":
        print("Description cannot be empty")
        return

    category = input("Enter expense category: ").strip().title()
    if category == "":
        print("Category cannot be empty.")
        return

    date = datetime.now().strftime("%d-%m-%Y")
    #Jis din expense add hua, us din ki date automatically save karo.

    expense_id = len(expenses) + 1
    expense = {
        "id":expense_id,
        "amount": amount,
        "description": description,
        "category": category,
        "date":date

    }

    expenses.append(expense)

    print("Expense added successfully.")


def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses available.")
        return

    print("\n---------- Your Expenses ----------")

    for i in range(len(expenses)):
        print("----------------------------")
        print(f"Expense Id : {expenses[i]['id']}")
        print(f"Amount  : ₹{expenses[i]['amount']:.2f}")
        print(f"Details : {expenses[i]['description']}")
        print(f"Category: {expenses[i]['category']}")
        print(f"Date    : {expenses[i]['date']}")


    print("----------------------------")

def total_expenses(expenses):

    if len(expenses) == 0:
        print("No expenses available.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total Expenses: ₹{total:.2f}")

def delete_expense(expenses):

    if len(expenses) == 0:
        print("No expenses available to delete.")
        return

    try:
        expense_number = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Please enter numbers only.")
        return

    if expense_number >= 1 and expense_number <= len(expenses):
        removed_expense = expenses.pop(expense_number - 1)

        print(
            f"₹{removed_expense['amount']:.2f} "
            f"({removed_expense['description']}) deleted successfully."
        )
    else:
        print("Invalid expense number.")

while True:
    show_menu()
    try:
        choice = int(input("Enter your choice: "))
    except  ValueError:
        print("Please enter numbers only.")
        continue

    if choice < 1 or  choice > 6 :
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
