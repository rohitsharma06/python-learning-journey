balance = 1000.0

def show_menu():
    print("========== ATM SIMULATOR ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("===================================")

while True:
    show_menu()

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Current Balance = ₹{balance:.2f}")
    elif choice == 2:

        try:
            amount = int(input("Enter Deposit Amount: "))
        except ValueError:
            print("Please enter a valid amount")
            continue

        if amount <= 0:
            print("Amount must be greater than 0")
            continue

        balance += amount

        print(f"₹{amount:.2f} added successfully")
        print(f"Current balance is : ₹{balance:.2f}")
    elif choice == 3:
        try:
            amount = float(input("Enter withdrawal amount: "))
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if amount <= 0:
            print("Amount must be greater than 0")
            continue

        if amount > balance:
            print("Insufficient balance.")
            continue

        balance -= amount

        print(f"₹{amount:.2f}  withdrawal successfully")
        print(f"Current balance is : ₹{balance:.2f}")

    elif choice == 4:
        print("Thank you For using ATM")
        break
    else:
        print("Please choose Valid option")

