from storage import save_expenses, load_expenses
from expenses import (
    add_expense,
    view_expenses,
    search_expenses,
    delete_expense,
    calculate_total
)


expenses = load_expenses()

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
        add_expense(expenses, save_expenses)

    elif choice == 2:
        view_expenses(expenses)

    elif choice == 3:
        calculate_total(expenses)

    elif choice == 4:
        delete_expense(expenses, save_expenses)

    elif choice == 5:
        search_expenses(expenses)

    elif choice == 6:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")