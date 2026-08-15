expenses = []

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
    print("Expense added successfully.")
def view_expenses():
    if not expenses:
        print("No expenses Found.")
        return

    print("\n========== EXPENSES ==========")
    for expense in expenses:
        print(f"Amount: ₹{expense['amount']}")
        print(f"Category: {expense['category']}")
        print(f"Description: {expense['description']}")
        print("------------------------------")

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
    print("4. Exit")
    print("=====================================")


while True:
    show_menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please Enter Valid choice ")
        continue

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        calculate_total()
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
